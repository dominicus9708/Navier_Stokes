# M19-212 — Orthogonal unit-kernel crossings have a skew first-order form; scalar self-pairing vanishes identically

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / CROSSING-FORM REDUCTION + MELNIKOV SELF-PAIRING NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Parameterized relative return

Let

\[
P(\lambda)\in SO(N)
\]

be a \(C^1\) family of certified symmetry-quotient hard relative returns on a fixed invariant finite-dimensional fiber. Let \(\lambda_0\) be a unit-kernel point and define

\[
P_0:=P(\lambda_0),
\qquad
K:=\ker(I-P_0).
\]

By M19-211, the finite hard Fredholm operator \(F_0=I-P_0\) has index zero and

\[
K=\ker F_0=\ker F_0^*.
\]

## 2. Orthogonality forces a skew infinitesimal generator

Differentiate

\[
P(\lambda)^TP(\lambda)=I
\]

at \(\lambda_0\). Then

\[
\dot P_0^TP_0+P_0^T\dot P_0=0.
\]

Hence

\[
\boxed{
A_0:=P_0^T\dot P_0
\quad\text{satisfies}\quad
A_0^T=-A_0.
}
\]

Let \(\Pi_K\) be the orthogonal projection onto the fixed space. The first-order crossing operator on the kernel is

\[
\boxed{
B_K:=\Pi_KA_0|_K.
}
\]

Because \(A_0\) is skew-adjoint,

\[
\boxed{B_K^T=-B_K.}
\]

Since \(P_0=I\) on \(K\) and \(P_0\) preserves \(K^\perp\), the same compression can be written as

\[
B_K=\Pi_K\dot P_0|_K.
\]

## 3. Scalar adjoint self-pairing vanishes

Take any fixed vector \(v\in K\). Since \(F=I-P\),

\[
\dot F_0=-\dot P_0.
\]

The natural scalar kernel/cokernel pairing is

\[
\langle v,\dot F_0v\rangle
=-\langle v,\dot P_0v\rangle.
\]

But skewness gives

\[
\langle v,\dot P_0v\rangle
=
\langle v,A_0v\rangle
=0.
\]

Therefore

\[
\boxed{
\langle v,\dot F_0v\rangle=0
\qquad\text{for every }v\in K.
}
\]

Thus a scalar same-vector Melnikov/Fredholm self-pairing cannot be the missing first-order kernel-exclusion mechanism. Its vanishing is structural, not an accidental cancellation of one profile.

## 4. Correct first-order object is an antisymmetric two-form

The nontrivial first-order information is instead

\[
\boxed{
\omega_K(v,w)
:=
\langle v,A_0w\rangle,
\qquad v,w\in K,
}
\]

with

\[
\omega_K(v,w)=-\omega_K(w,v).
\]

Equivalently, \(\omega_K\) is represented by the skew matrix \(B_K\).

If \(\dim K\) is odd, every skew matrix on \(K\) is singular. Therefore at least one kernel direction cannot be removed to first order by a one-parameter orthogonal deformation. This agrees with the parity obstruction of M19-211.

## 5. Two-dimensional kernel crossing

On an even-dimensional symmetry quotient, the minimal residual kernel has real dimension two. Choose an orthonormal basis \((e_1,e_2)\) of such a kernel block. Then

\[
B_K=
\begin{pmatrix}
0&-\beta\\
\beta&0
\end{pmatrix}
\]

for some real \(\beta\).

If

\[
\boxed{\beta\ne0,}
\]

then the two unit eigenvalues split to first order as a conjugate pair

\[
\boxed{
\mu_\pm(\lambda)
=
\exp\!\left(\pm i\beta(\lambda-\lambda_0)
+o(|\lambda-\lambda_0|)\right).
}
\]

Thus \(\beta\ne0\) means the unit resonance is **transversal**, not impossible. The kernel disappears on nearby parameter values but still exists at \(\lambda_0\).

Correspondingly,

\[
\det(I-P(\lambda))
\sim
C\,\beta^2(\lambda-\lambda_0)^2
\]

with \(C>0\) from the nonresonant blocks, confirming the M19-211 determinant-sign no-go.

If \(\beta=0\), the degeneracy is higher order and requires second-order or profile-specific analysis.

## 6. Identification with the M19-204 resonance phase

For one nontrivial RDSS real rotation block, M19-204 gives the kernel resonance

\[
\Theta(\lambda)
:=
\kappa(\lambda)L(\lambda)-\phi(\lambda)
\in2\pi\mathbb Z.
\]

The corresponding relative return block is rotation by \(\Theta\) modulo \(2\pi\). At a kernel point \(\Theta(\lambda_0)=2\pi n\), the crossing coefficient is, up to the orientation convention of the chosen real basis,

\[
\boxed{
\beta
=
\Theta'(\lambda_0)
=
\frac d{d\lambda}
\bigl(\kappa L-\phi\bigr)_{\lambda=\lambda_0}.
}
\]

Thus the abstract Fredholm crossing form and the exact finite resonance law are the same first-order object in two representations.

## 7. Generic transversality is not a theorem of nonexistence

If \(\beta\ne0\), a kernel resonance is locally isolated in a one-parameter family. In a multiparameter family, a nonzero gradient of \(\Theta\) generically gives a codimension-one resonance set.

But the Millennium-problem proof cannot discard such a set as merely nongeneric. A single admissible profile/parameter point with a nonsymmetry unit kernel remains a survivor.

Permanent firewall:

\[
\boxed{
\text{transversal/codimension-one degeneracy}
\neq
\text{degeneracy exclusion}.
}
\]

## 8. Revised next analytic target

The finite-amplitude RSS/RDSS frontier is now more precise.

Scalar activity bounds failed at M19-210. Determinant-sign topology failed at M19-211. Scalar adjoint self-pairing fails identically at M19-212.

The next useful object must be one of:

1. a **PDE formula for the skew crossing coefficient** \(\beta\) or higher-dimensional two-form \(\omega_K\), combined with a global phase obstruction rather than mere transversality;
2. a **spectral-angle/winding argument** proving \(\Theta\notin2\pi\mathbb Z\) on the entire admissible moderate compact set;
3. a **profile-specific signed identity** that directly forbids a fixed vector of the relative return.

No current module supplies any of these globally, so the bounded-period branch remains OPEN.
