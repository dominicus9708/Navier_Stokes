# DSD M19-168 — The real scattering isometry makes the quotient hard monodromy orthogonal, so genuine irrational elliptic obstructions require at least two real dimensions

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / REAL-ORTHOGONAL UNIT-SPECTRUM STRUCTURE / ELLIPTIC DIMENSION REDUCTION / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

The remaining unit-spectrum problem contains

- fixed-moduli `mu=1` kernel directions;
- rational elliptic phases, already reducible to finite-iterate kernels;
- genuinely irrational elliptic phases.

M19-167 closed the direct tensor shortcut. The present module uses the real structure of the Navier--Stokes linearization and the exact scattering isometry to constrain the possible elliptic blocks.

## 2. Real quotient hard fiber

The linearized Navier--Stokes equation has real coefficients.
After removing the exact time/rotation symmetry representation, let

\[
E_q^{hard}(U)
\]

be the real finite-dimensional quotient hard fiber.

The scattering pullback metric is real and positive definite on this fiber.

Exact differentiated scattering covariance gives

\[
\|\Phi_t v\|_{sc,\sigma_tU}
=
\|v\|_{sc,U}.
\]

For a relative-periodic orbit, identify the terminal fiber with the initial fiber using the physical holonomy rotation. The resulting quotient twisted monodromy satisfies

\[
\boxed{
\mathcal M_{q}^{tw}
\in
O(N),
\qquad
N=\dim_{\mathbb R}E_q^{hard}.
}
\]

## 3. Orientation on a continuous stratum

The linearized flow begins at the identity and depends continuously on time/background.
The spatial rotation holonomy belongs to the connected group `SO(3)`, and its induced representation on a fixed real hard-fiber stratum varies continuously from the identity representation.

Hence, after a continuous real trivialization on a connected orientation-preserving stratum,

\[
\boxed{
\det\mathcal M_q^{tw}=+1,
}
\]

so

\[
\boxed{
\mathcal M_q^{tw}\in SO(N).
}
\]

If a bundle-orientation change prevents this trivialization, that is a separate typed bundle-topology stratum rather than a hidden spectral conclusion.

## 4. Real spectral decomposition

Every real orthogonal matrix decomposes into blocks of the form

\[
[1],
\qquad
[-1],
\qquad
R(\vartheta)
=
\begin{pmatrix}
\cos\vartheta&-\sin\vartheta\\
\sin\vartheta&\cos\vartheta
\end{pmatrix}.
\]

Thus every nonreal unit multiplier

\[
e^{i\vartheta}
\]

appears with its conjugate

\[
e^{-i\vartheta}
\]

and occupies a **two-dimensional real invariant plane**.

Therefore

\[
\boxed{
\text{genuine elliptic block}
\Longrightarrow
\dim_{\mathbb R}E_q^{hard}\ge2.
}
\]

## 5. Irrational elliptic obstruction needs dimension at least two

A genuinely new elliptic obstruction has

\[
\frac{\vartheta}{2\pi}\notin\mathbb Q.
\]

Such a mode cannot occur in a one-dimensional real invariant space.

Hence

\[
\boxed{
\dim_{\mathbb R}E_q^{hard}\le1
\Longrightarrow
\text{no irrational elliptic neutral block}.
}
\]

This is a substantial weakening of the previous elliptic target.

One does not need to exclude irrational phases one by one if the quotient hard dimension can first be reduced to at most one.

## 6. What remains in one dimension

If

\[
N=1,
\]

then

\[
\mathcal M_q^{tw}\in O(1)=\{+1,-1\}.
\]

Thus the only possibilities are

\[
\boxed{
\mu=+1
\quad\text{or}\quad
\mu=-1.
}
\]

The `+1` case is the ordinary fixed-moduli kernel.

The `-1` case satisfies

\[
(\mathcal M_q^{tw})^2=I,
\]

so it becomes a kernel direction for the two-fold iterate.

Therefore

\[
\boxed{
N\le1
\Longrightarrow
\text{all residual unit spectrum reduces to a finite-iterate kernel problem}.
}
\]

## 7. Determinant parity

On an orientation-preserving `SO(N)` stratum, the number of `-1` eigenvalues is even.

Hence if

\[
N=1
\]

and the quotient monodromy is genuinely in `SO(1)`, then

\[
\boxed{
\mathcal M_q^{tw}=+1.
}
\]

Thus the one-dimensional quotient obstruction is directly a `mu=1` kernel.

The `-1` option can arise only if the relevant real quotient bundle/identification reverses orientation or if one works before the orientation-preserving stratum is fixed.

## 8. Revised strategic target

The previous hard target was

\[
\text{exclude all irrational elliptic phases}.
\]

The present result allows the weaker two-step target

\[
\boxed{
\dim_{\mathbb R}E_q^{hard}\le1
}
\]

followed by

\[
\boxed{
\text{finite-iterate kernel rigidity}.
}
\]

This is potentially easier because M19-159--162 already convert hard-mode multiplicity into compact-core compensation eigenchannel counts and collective anisotropy.

## 9. Relation to compensation counting

If one can prove that after exact symmetry modes there is room for at most one additional superthreshold compensation channel, then

\[
\dim E_q^{hard}\le1
\]

provided every quotient hard mode is unit/zero-growth on the observable bundle.

M19-132--133 supply precisely that zero-growth/isometric structure.

Therefore a **one-extra-channel bound** is already sufficient to eliminate the genuinely irrational elliptic problem.

One does not need the stronger zero-extra-channel bound until the final finite-iterate kernel step.

## 10. Evans/characteristic polynomial viewpoint

For completeness define

\[
P_U(z)
:=
\det
\left(
zI-\mathcal M_q^{tw}
\right).
\]

Because the matrix is real orthogonal,

\[
P_U(z)
\]

has real coefficients and its nonreal unit roots occur in conjugate reciprocal pairs.

However this characteristic polynomial does not itself exclude unit roots; it only packages the finite-dimensional unit-spectrum problem.

Permanent firewall:

\[
\boxed{
\text{finite Evans polynomial}
\neq
\text{nonvanishing Evans polynomial}.
}
\]

## 11. Audit verdict

### Proved

1. The real symmetry-quotient hard monodromy is orthogonal in the scattering pullback metric.
2. On an orientation-preserving continuous stratum it lies in `SO(N)`.
3. Every genuine irrational elliptic block requires at least two real quotient dimensions.
4. If the quotient hard dimension is at most one, all residual unit spectrum reduces to a finite-iterate kernel problem.

### Not proved

1. The dimension bound `dim E_q^{hard}<=1`.
2. Kernel rigidity.
3. Global regularity.

## 12. Next target

M19-169 should combine M19-159's compensation-channel count with the present real-dimension observation and formulate the weakest sufficient spectral-count condition:

\[
\boxed{
N_{comp}(\Lambda_*)
\le
 d_{sym}+1.
}
\]

Such a bound would eliminate all genuinely irrational elliptic blocks at once and leave only one finite-iterate kernel channel to close.
