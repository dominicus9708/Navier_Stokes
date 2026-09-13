# M19-230 — The affine interior adjoint correction reduces to a compact zero-boundary period map, but large spectator radius does not give a Poincaré contraction

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / BOUNDED-CYLINDER FREDHOLM REDUCTION + LARGE-R CONTRACTION NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-229 localizes the bounded-period adjoint problem to the relative-periodic Calderón range on a finite spectator cylinder. The remote critical adjoint datum is first transported to the spectator sphere by the invertible transpose-scattering map, and then one subtracts a fixed lifting of those boundary/asymptotic data.

The remaining unknown is a zero-boundary interior adjoint correction with an affine forcing/return defect.

This module reduces that correction problem to a compact period-map Fredholm equation and tests the simplest possible contraction argument.

## 2. Interior correction after a fixed lifting

Fix a sufficiently remote radius R and period S. Let \(\Psi^{lift}\) be any smooth extension into \(B_R\times[0,S]\) of the finite-spectator adjoint trace induced by the remote critical dual datum. It need not solve the interior adjoint PDE.

Write

\[
\Psi=\Psi^{lift}+Z.
\]

Choose the lifting so that the correction has homogeneous boundary data

\[
\boxed{Z|_{S_R}=0}
\]

and impose the solenoidal constraint in the standard projected formulation.

Then Z solves an inhomogeneous backward parabolic system

\[
\boxed{
-\partial_s Z
=L_U^*(s)Z+F_R(s),
\qquad Z|_{S_R}=0,
}
\]

where \(F_R\) is determined entirely by the chosen lifting.

The relative-periodic return is affine because the lifting need not itself match the holonomy:

\[
\boxed{
Z(S)=\mathcal R_{Q_*}Z(0)+g_R,
}
\]

with a known defect \(g_R\).

## 3. Forward-time zero-boundary adjoint evolution

Set

\[
\tau=S-s,
\qquad
z(\tau)=Z(S-\tau).
\]

Then

\[
\boxed{
\partial_\tau z
=L_U^*(S-\tau)z+\widetilde F_R(\tau),
\qquad z|_{S_R}=0.
}
\]

Let

\[
\mathcal U_R^{ad}(\tau,\sigma)
\]

be the homogeneous zero-boundary evolution operator.

Duhamel gives

\[
z(S)
=
\mathcal U_R^{ad}(S,0)z(0)
+
\int_0^S
\mathcal U_R^{ad}(S,\tau)\widetilde F_R(\tau)d\tau.
\]

After composing with the relative rotation, the affine periodicity condition can be written

\[
\boxed{
(I-\mathcal M_R^{ad})z_0=h_R,
}
\]

for a known \(h_R\), where, up to the fixed convention for whether the rotation is placed at the initial or final end,

\[
\boxed{
\mathcal M_R^{ad}
:=
\mathcal R_{Q_*}^{-1}\mathcal U_R^{ad}(S,0).
}
\]

The exact placement of \(\mathcal R_{Q_*}^{\pm1}\) changes no spectral conclusion because the rotation is bounded and invertible.

## 4. Compactness of the period map

On the bounded smooth ball \(B_R\), the zero-boundary linear parabolic evolution gains positive spatial regularity for every positive time. Under the retained smooth coefficient bounds, for example,

\[
\mathcal U_R^{ad}(S,0):L^2_\sigma(B_R)
\longrightarrow
H^1_0(B_R)\cap L^2_\sigma(B_R)
\]

boundedly for fixed \(S>0\).

The embedding

\[
H^1_0(B_R)\Subset L^2(B_R)
\]

is compact. Hence

\[
\boxed{
\mathcal M_R^{ad}:L^2_\sigma(B_R)\to L^2_\sigma(B_R)
\text{ is compact.}
}
\]

Therefore

\[
\boxed{
I-\mathcal M_R^{ad}
\text{ is Fredholm of index }0.
}
\]

Its kernel and cokernel are finite dimensional.

## 5. Exact Fredholm compatibility for the affine correction

The equation

\[
(I-\mathcal M_R^{ad})z_0=h_R
\]

is solvable if and only if

\[
\boxed{
\langle h_R,\varphi\rangle=0
\qquad
\forall
\varphi\in\ker(I-(\mathcal M_R^{ad})^*)
}
\]

in the chosen Hilbert realization.

The adjoint of the zero-boundary adjoint monodromy is the corresponding primal zero-boundary relative monodromy, up to the same rotation convention. Thus the only obstruction to the affine interior adjoint extension is a finite-dimensional space of zero-boundary primal unit modes on the spectator ball.

This is a genuine dimensional reduction:

\[
\boxed{
\text{infinite-dimensional interior range problem}
\longrightarrow
\text{finite-dimensional unit-multiplier compatibility}.}
\]

It is not yet kernel exclusion.

## 6. Energy identity for the homogeneous adjoint correction

For the forward-time homogeneous adjoint evolution

\[
\partial_\tau z=L_U^*(S-\tau)z,
\qquad z|_{S_R}=0,
\]

the unweighted L2 energy satisfies

\[
\frac12\frac d{d\tau}\|z\|_2^2
=
-\nu\|\nabla z\|_2^2
+\frac14\|z\|_2^2
-
\int_{B_R} z^TS_Uz\,dy.
\]

Indeed the adjoint dilation drift contributes

\[
\int z\cdot\frac12(y\cdot\nabla)z
=-\frac34\|z\|_2^2
\]

under the zero Dirichlet boundary condition, while the adjoint zeroth-order term contributes \(+\|z\|_2^2\).

Hence

\[
\boxed{
\frac12\frac d{d\tau}\|z\|_2^2
\le
-\nu\|\nabla z\|_2^2
+
\left(\frac14+\|S_U\|_{L^\infty(B_R)}\right)
\|z\|_2^2.
}
\]

## 7. Poincaré contraction condition points in the wrong radius direction

Let \(\lambda_1(R)\) be the first Dirichlet Laplacian eigenvalue on \(B_R\). Then

\[
\|\nabla z\|_2^2
\ge
\lambda_1(R)\|z\|_2^2,
\qquad
\lambda_1(R)=R^{-2}\lambda_1(1).
\]

Therefore a sufficient uniform contraction condition is

\[
\boxed{
\nu\lambda_1(R)
>
\frac14+\sup_s\|S_U(s)\|_{L^\infty(B_R)}.
}
\]

But

\[
\lambda_1(R)\sim R^{-2}.
\]

Thus increasing R weakens the Poincaré gap. The spectator construction requires R to be sufficiently large, whereas the elementary Dirichlet Poincaré contraction is strongest for small R.

Consequently

\[
\boxed{
\text{sufficiently remote spectator radius}
\not\Rightarrow
\text{zero-boundary adjoint period-map contraction}.
}
\]

The remote-tail smallness does not help because a zero-boundary interior mode can remain concentrated in the finite core where \(S_U\) is order one.

## 8. No automatic unit-gap from compactness

Compactness implies that every nonzero spectral value of \(\mathcal M_R^{ad}\) is an isolated eigenvalue of finite multiplicity, accumulating only at zero.

It does not imply

\[
1\notin\sigma(\mathcal M_R^{ad}).
\]

Hence

\[
\boxed{
\text{compact period map}
\neq
\text{unit-multiplier exclusion}.
}
\]

The new reduction is finite-dimensional, not coercive.

## 9. Relation to the original whole-space hard kernel

The zero-boundary unit modes of the artificial ball problem are not automatically the same as the original whole-space hard resonances. They arise as cokernel obstructions to extending the independently transported critical dual datum through the interior.

This is potentially a smaller problem because:

1. it is posed on a bounded smooth cylinder;
2. its obstruction space is finite dimensional by compact parabolic monodromy;
3. the remote critical data enter only through the explicit affine vector \(h_R\).

But it is not yet certified to be strictly easier. The compatibility pairing with \(h_R\) may encode exactly the same whole-space resonance information in another form.

Permanent firewall:

\[
\boxed{
\text{finite-dimensional cavity obstruction}
\neq
\text{independent kernel exclusion until its relation to }h_R\text{ is controlled}.
}
\]

## 10. Updated bounded-period target

The refined theorem can be stated as

\[
\boxed{
\mathcal T_{cav}^{comp}:
\text{for the affine vector }h_R\text{ induced by the nondegenerate critical dual lifting,}
\ 
h_R\perp\ker(I-(\mathcal M_R^{ad})^*)
}
\]

for at least one sufficiently remote spectator radius R, by an argument independent of assuming whole-space kernel-freeness.

Equivalently, one may seek a radius at which \(1\notin\sigma(\mathcal M_R^{ad})\), but the simple large-R Poincaré estimate does not provide it.

## 11. Certified / not certified

### Certified

1. The lifted interior adjoint problem reduces to an affine zero-boundary relative-periodic parabolic correction.
2. Its homogeneous period map is compact on the bounded spectator ball.
3. I minus the period map is Fredholm index zero.
4. Solvability reduces to finitely many unit-multiplier compatibility conditions.
5. A simple Dirichlet Poincaré contraction is strongest at small R and does not follow from the required large spectator radius.

### Not certified

1. Exclusion of unit multipliers of the cavity monodromy.
2. Compatibility of h_R with all cavity cokernel modes.
3. Strict independence of the cavity obstruction from the original whole-space hard kernel.
4. Bounded-period kernel exclusion.
5. Global regularity.

## 12. Next target

Study the R-dependence of the finite-dimensional cavity compatibility pairing. The key question is whether the critical remote lifting forces a nonzero asymptotic sign/limit of the compatibility determinant as R tends to infinity, while cavity unit modes remain core-localized, or whether the Green identity makes the pairing identically equivalent to the original resonance obstruction.
