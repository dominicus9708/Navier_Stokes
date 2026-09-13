# M19-211 — Relative hard return parity, fixed-space decomposition, and determinant-sign no-go

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / PARITY REDUCTION + INDEX NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Certified finite-dimensional relative return

Work on a certified finite-dimensional **symmetry-quotient hard fiber** \(H_q\) of real dimension

\[
N:=\dim H_q.
\]

M19-202 gives a continuous orthogonal scattering-translation representation on the hard bundle. After the exact time/rotation bookkeeping used in M19-202--204, the relative return on a bounded-period RSS/RDSS hard fiber is an orthogonal map. On any retained quotient fiber on which the induced rotation holonomy is represented continuously from the identity component, both the time action and the holonomy action are orientation preserving. Hence the relative return satisfies

\[
\boxed{P_{rel}\in SO(N).}
\]

This statement is made only on the certified invariant quotient hard fiber; loss of that invariant identification remains a compactness/domain exit rather than being silently absorbed here.

## 2. Real spectral decomposition

Every real \(P_{rel}\in SO(N)\) admits an orthogonal decomposition into

- a \(+1\) fixed subspace of dimension \(m_+\);
- a \(-1\) subspace of dimension \(m_-\);
- real two-dimensional rotation blocks with eigenvalues \(e^{\pm i\theta_j}\), \(0<\theta_j<\pi\).

Thus

\[
N=m_++m_-+2J.
\]

Since \(\det P_{rel}=1\), the multiplicity \(m_-\) is even. Therefore

\[
\boxed{m_+\equiv N\pmod 2.}
\]

This is the first parity constraint on the symmetry-quotient unit kernel.

## 3. Odd residual hard dimension forces a +1 kernel

If

\[
N\ \text{is odd},
\]

then the parity relation gives

\[
\boxed{m_+\ge1.}
\]

Hence an odd-dimensional symmetry-quotient hard return cannot be kernel-free. A residual \(+1\) direction is forced by orientation-preserving orthogonal geometry.

Therefore the desired bounded-period rigidity theorem can hold only if one of the following happens:

1. the true symmetry-quotient hard dimension is even; or
2. the apparently residual odd fixed direction is actually an omitted exact symmetry and the quotient has not yet been completed correctly.

This extends M19-202, which treated the special case \(N\le1\).

Conversely, if \(N\) is even, then

\[
\boxed{m_+\ \text{is even}.}
\]

Thus a nonsymmetry \(+1\) degeneracy on an even-dimensional certified quotient cannot be a single simple real fixed direction; it occurs with even real multiplicity.

## 4. Compatibility with the M19-204 resonance law

M19-204 gives, on every nontrivial RDSS frequency/holonomy block,

\[
\kappa L+\vartheta-\phi=2\pi n.
\]

For a kernel, \(\vartheta=0\), so

\[
\kappa L-\phi=2\pi n.
\]

Every nonzero resonant complex channel appears as a two-dimensional real rotation block. Thus the finite resonance description and the parity result agree: nontrivial unit resonances contribute in real dimension two. Any unpaired one-dimensional fixed direction belongs to the zero/trivial representation sector and must be checked against the exact symmetry quotient.

## 5. Fredholm index and adjoint fixed space

Define the finite hard Fredholm operator

\[
F:=I-P_{rel}.
\]

Because the hard fiber is finite-dimensional,

\[
\operatorname{ind}F=0.
\]

Moreover orthogonality gives

\[
P_{rel}^{-1}=P_{rel}^T.
\]

Therefore

\[
P_{rel}v=v
\iff
P_{rel}^Tv=v,
\]

and hence

\[
\boxed{
\ker(I-P_{rel})
=
\ker(I-P_{rel})^*.
}
\]

Thus every residual unit kernel automatically carries an adjoint cokernel witness in the same fixed subspace with respect to the scattering-induced orthogonal metric.

## 6. Determinant of the fixed-point operator

For the above spectral decomposition,

\[
\det(I-P_{rel})=0
\]

when \(m_+>0\). If \(m_+=0\), then

\[
\det(I-P_{rel})
=
2^{m_-}
\prod_{j=1}^{J}
\bigl(1-e^{i\theta_j}\bigr)
\bigl(1-e^{-i\theta_j}\bigr),
\]

so

\[
\boxed{
\det(I-P_{rel})
=
2^{m_-}
\prod_{j=1}^{J}4\sin^2\frac{\theta_j}{2}
>0.
}
\]

Consequently, for every orientation-preserving orthogonal relative return,

\[
\boxed{\det(I-P_{rel})\ge0.}
\]

## 7. Determinant-sign index is a no-go

Consider a continuous parameter family \(P_{rel}(\lambda)\in SO(N)\). When a conjugate pair \(e^{\pm i\theta(\lambda)}\) crosses \(+1\), the corresponding determinant factor is

\[
4\sin^2\frac{\theta(\lambda)}2.
\]

Near a transversal crossing \(\theta(\lambda_0)=0\),

\[
4\sin^2\frac{\theta(\lambda)}2
\sim
\theta'(\lambda_0)^2(\lambda-\lambda_0)^2.
\]

Thus the determinant touches zero with even order and does **not** change sign.

Therefore

\[
\boxed{
\text{sign}\,\det(I-P_{rel})
\text{ cannot serve as the missing kernel-exclusion index.}
}
\]

A naive \(\mathbb Z_2\) orientation/degree argument based only on the sign of the Fredholm determinant is structurally blind to these orthogonal unit-kernel crossings.

## 8. Revised bounded-period theorem frontier

M19-210 showed that lower activity observability cannot supply the upper-smallness needed by contraction. M19-211 further removes a second overly coarse route: determinant-sign topology.

The finite-amplitude RSS/RDSS kernel problem now splits into two exact structural tasks:

\[
\boxed{
\text{(A) certify an even-dimensional complete symmetry quotient,}
}
\]

and, on that quotient,

\[
\boxed{
\text{(B) exclude two-dimensional }(+1)\text{ resonance crossings/block fixed spaces.}
}
\]

The remaining mechanism must therefore resolve **spectral angle/winding, a skew crossing form, or a profile-specific signed PDE pairing**, rather than scalar activity size or determinant sign.

## 9. Firewall

This module does **not** prove kernel nonexistence. In particular, odd residual dimension would imply a kernel rather than a contradiction. The result is a parity reduction and a topological no-go that sharply identifies the next calculation.
