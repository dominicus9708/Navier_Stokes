# M19-229 — The remaining bounded-period adjoint problem is a finite-spectator relative-periodic Calderón trace-range problem

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / INTERIOR ADJOINT TRACE-RANGE NORMAL FORM

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-227 transports every critical dual functional between infinity and a sufficiently remote finite spectator sphere without loss. M19-228 supplies an explicit nondegenerate dual functional for every finite hard resonance.

What remains is not an abstract dual-space problem. A dual functional must be represented by the Cauchy trace of an actual relative-periodic solution of the physical backward adjoint PDE in the interior.

This module writes that distinction as an exact finite-boundary trace-range problem.

## 2. Finite spectator cylinder

Fix a sufficiently remote similarity radius R and one bounded relative period S. Let

\[
\Omega_R:=B_R,
\qquad
\Sigma_R:=S_R\times[0,S].
\]

The background obeys the relative return

\[
U(S)=\mathcal R_{Q_*}U(0)
\]

in the natural rotation action.

A primal relative-periodic linearized state satisfies

\[
\mathcal P_UW:=\partial_sW-L_UW+\nabla Q=0,
\qquad
W(S)=\mathcal R_{Q_*}W(0),
\]

and a backward adjoint state satisfies

\[
\mathcal P_U^*\Psi:=-\partial_s\Psi-L_U^*\Psi-\nabla\Pi=0,
\qquad
\Psi(S)=\mathcal R_{Q_*}\Psi(0),
\]

with both fields divergence free.

## 3. Exact one-period boundary Green form

For any such primal/adjoint pair, the finite-ball Green identity of M19-225 integrates over one period to

\[
\boxed{
\int_0^S\int_{S_R}
\Bigl[
\nu(\Psi\cdot\partial_nW-W\cdot\partial_n\Psi)
-(b\cdot n)W\cdot\Psi
-Q\Psi\cdot n
-\Pi W\cdot n
\Bigr]\,dS\,ds
=0,
}
\]

because the volume pairing at s=0 and s=S is equal by the relative rotation law.

Define the boundary bilinear/Hermitian concomitant

\[
\boxed{
\mathfrak B_R\bigl(\Gamma_R^{pr}(W,Q),\Gamma_R^{ad}(\Psi,\Pi)\bigr)
}
\]

by the integral above, where \(\Gamma_R^{pr}\) and \(\Gamma_R^{ad}\) denote the full boundary Cauchy data required by the expression (velocity trace, normal derivative/traction, and pressure trace modulo gauge).

## 4. Relative-periodic Calderón trace sets

Define the primal trace set

\[
\boxed{
\mathcal C_R^{pr}
:=
\left\{
\Gamma_R^{pr}(W,Q):
\mathcal P_UW=0,
\ W(S)=\mathcal R_{Q_*}W(0)
\right\}
}
\]

and the adjoint trace set

\[
\boxed{
\mathcal C_R^{ad}
:=
\left\{
\Gamma_R^{ad}(\Psi,\Pi):
\mathcal P_U^*\Psi=0,
\ \Psi(S)=\mathcal R_{Q_*}\Psi(0)
\right\}.
}
\]

Then the exact Green identity gives the inclusion

\[
\boxed{
\mathfrak B_R(G,H)=0
\qquad
\forall G\in\mathcal C_R^{pr},
\ \forall H\in\mathcal C_R^{ad}.
}
\]

This is the finite-spectator Calderón orthogonality relation.

No stronger equality between the annihilator of one trace set and the other trace set is asserted here; such a statement would require an additional well-posedness/Fredholm theorem.

## 5. What the remote transpose actually supplies

M19-227 starts from a critical far-field dual datum c_b and gives a nondegenerate finite-spectator dual functional

\[
\boxed{
\lambda_R\in(\text{primal spectator trace space})^*.
}
\]

It satisfies norm comparability with the far-field critical pairing and, on the retained hard mode trace G_b, remains nonzero for sufficiently remote R.

But

\[
\boxed{
\lambda_R\text{ is an abstract boundary functional.}
}
\]

For it to be represented by a physical interior adjoint state, there must exist

\[
H\in\mathcal C_R^{ad}
\]

such that

\[
\boxed{
\lambda_R(G)
=
\mathfrak B_R(G,H)
}
\]

on the relevant primal hard trace space.

That is the exact missing range condition.

## 6. Why Banach-dual representation is weaker

M19-131 implies that finite hard observability makes the transpose observation map surjective onto the finite hard dual.

Therefore every hard covector can be represented by some linear functional on spectator data.

However the set

\[
\left\{
G\mapsto\mathfrak B_R(G,H):H\in\mathcal C_R^{ad}
\right\}
\]

is a PDE-selected subset of the full Banach dual.

Hence

\[
\boxed{
\text{hard covector represented by a boundary functional}
\neq
\text{hard covector represented by a relative-periodic adjoint Cauchy trace}.
}
\]

This is the finite-boundary form of the M19-226 circularity firewall.

## 7. Exact remaining range theorem

Let E_R^{hard} be the finite-dimensional space of retained primal hard Cauchy traces at the spectator sphere.

Define the adjoint trace-to-hard-dual map

\[
\boxed{
\mathcal A_R:
\mathcal C_R^{ad}
\longrightarrow
(E_R^{hard})^*,
\qquad
\mathcal A_R(H)[G]
:=
\mathfrak B_R(G,H).
}
\]

Because every actual primal/adjoint homogeneous relative-periodic pair has zero Green pairing, the relevant use is not arbitrary homogeneous H paired with the same primal kernel; rather one must formulate the physical dual extension with the remote asymptotic datum included in the global Cauchy data. Equivalently, after subtracting a fixed remote lifting of c_b, the interior correction problem asks whether a specific affine hard-dual class lies in the range of the homogeneous interior trace operator.

This makes the noncircular target precise:

\[
\boxed{
\mathcal T_{Cal}^{int}:
\text{determine the relative-periodic adjoint Calderón range for the affine data induced by the remote critical dual lifting.}
}
\]

The affine forcing/lifting formulation prevents one from silently replacing the physical adjoint extension problem by arbitrary homogeneous dual surjectivity.

## 8. Is this smaller than the original kernel theorem?

Not yet certified.

The trace formulation is useful because it localizes the obstruction to a bounded spatial cylinder with smooth coefficients and separates three layers:

1. remote critical dual transport — already invertible by M19-227;
2. finite-boundary trace representation — explicit through the Green concomitant;
3. interior relative-periodic correction/range — still OPEN.

But M19-229 does not prove that layer 3 is analytically easier than the original whole-space hard-kernel problem.

Permanent firewall:

\[
\boxed{
\text{Calderón range reformulation}
\neq
\text{Calderón range surjectivity or kernel exclusion}.
}
\]

## 9. Next target

Analyze the affine interior correction problem after subtracting the independently constructed remote adjoint lifting. The natural object is the zero-boundary relative-periodic adjoint period map on B_R. Determine whether its unit multiplier can be excluded for at least one sufficiently remote spectator radius, or whether such a statement is again equivalent to the original bounded-period kernel frontier.
