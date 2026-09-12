# DSD M19-161 — Birman--Schwinger localization shows all superthreshold compensation channels live in a finite compact core while the critical r^-2 tail is CLR-borderline

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / EIGENCHANNEL-COUNT LOCALIZATION / CRITICAL-TAIL BORDERLINE IDENTIFIED / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-159 reduced nonsymmetry kernel rigidity to an eigenvalue-count condition for the compact-core compensation operator. M19-160 showed that neither trace-free strain nor compactness gives a one-channel rank bound for free.

The present module asks where eigenchannels above the enhanced threshold

\[
\Lambda_1
=
\frac14+\nu\lambda_{P,1}
\]

can live.

The answer is useful even though it does not yet close the count:

\[
\boxed{
\text{every genuinely superthreshold channel can be localized to a finite compact core.}
}
\]

The far critical tail is form-small, while the naive global CLR integral is exactly borderline for the `r^-2` strain decay.

## 2. Tail/core split

Choose a large radius `R` and decompose

\[
S_U
=
S_{core,R}
+
S_{tail,R},
\]

where

\[
S_{core,R}=\chi_R S_U,
\qquad
S_{tail,R}=(1-\chi_R)S_U.
\]

Likewise split the gradient-vorticity coupling

\[
K_{\nabla\Omega}
=
K_{core,R}^{nl}
+
K_{tail,R}^{nl}.
\]

The retained critical tail has

\[
|S_U(y)|\lesssim |y|^{-2},
\qquad
|\nabla\Omega(y)|\lesssim |y|^{-3}.
\]

By M19-095 and M19-150, the tail perturbation is relatively compact and its quadratic form becomes arbitrarily small compared with the bare vorticity coercive form as `R->infinity`.

Thus for every

\[
0<\varepsilon<\Lambda_1,
\]

one can choose `R=R(epsilon)` so that

\[
\boxed{
|\mathcal C_{tail,R}[W]|
\le
\varepsilon
\left(
\|\eta\|_2^2
+
\nu\|\nabla\eta\|_2^2
\right)
}
\]

for all normalized hard perturbations in the retained corridor.

## 3. Superthreshold channels cannot be tail-only

Suppose a normalized hard direction has total compensation Rayleigh quotient at least `Lambda_1`.

After choosing `epsilon` much smaller than the strict gap between the desired threshold and the tail form bound, the tail cannot supply that Rayleigh quotient by itself.

Therefore

\[
\boxed{
\text{every channel with }\kappa_j\ge\Lambda_1
\text{ has a quantitatively nontrivial compact-core component.}
}
\]

This is the eigenchannel-count version of the compact-core activity floor from M19-150.

## 4. Why a naive global CLR integral is borderline

For the local strain part, the natural static comparison operator is schematically

\[
\mathscr A_S
=
\nu(-\Delta)
+
\Lambda
-
S_U(y)
\]

on divergence-free vector fields, where `Lambda` is a positive threshold.

A Cwikel--Lieb--Rozenblum type bound in three dimensions would involve an integral of the positive matrix potential at power `3/2`:

\[
N_-
\lesssim
\nu^{-3/2}
\int
\operatorname{tr}
\left[(S_U-\Lambda I)_+^{3/2}\right]dy
\]

or a comparable matrix-valued Birman--Schwinger quantity.

But the critical tail has

\[
|S_U(y)|\sim r^{-2}.
\]

Hence formally

\[
|S_U|^{3/2}
\sim
r^{-3},
\]

and

\[
\int_{r>R}
r^2r^{-3}dr
\sim
\int_R^\infty\frac{dr}{r}.
\]

Thus

\[
\boxed{
S_U=O(r^{-2})
\text{ is exactly CLR-borderline in three dimensions.}
}
\]

This explains why a global scalar `L^{3/2}` count is not the correct way to exploit the critical tail.

## 5. Threshold saves the tail count

The relevant count is not the count of all positive strain eigenvalues. It is the count of eigenchannels capable of overcoming a **strict positive threshold** `Lambda_1`.

Since

\[
|S_U(y)|\to0
\qquad(r\to\infty),
\]

there exists a finite radius `R_Lambda` such that

\[
\|S_U(y)\|_{op}
<
\frac{\Lambda_1}{4}
\qquad
|y|>R_{\Lambda}.
\]

Together with the form-small nonlocal tail, the far region cannot create a superthreshold compensation channel.

Therefore the superthreshold count is controlled entirely by the finite region

\[
\boxed{B_{R_{\Lambda}}.}
\]

The logarithmic divergence of the unthresholded CLR integral is therefore a **borderline bookkeeping issue**, not a source of infinitely many hard superthreshold channels.

## 6. Finite-core Birman--Schwinger count

Inside the fixed ball `B_R`, the background is smooth and bounded.

Let

\[
M_S(R)
:=
\|S_U\|_{L^\infty(B_R)}.
\]

Ignoring for the moment the compact nonlocal term, the number of local strain channels capable of overcoming a positive level `Lambda` is bounded by the finite-volume spectral count for

\[
\nu(-\Delta)+\Lambda-M_{S}(R).
\]

A Weyl/CLR-type estimate gives schematically

\[
\boxed{
N_{strain}(\Lambda;R)
\lesssim
R^3
\left(
\frac{(M_S(R)-\Lambda)_+}{\nu}
\right)^{3/2},
}
\]

up to universal/domain constants and the divergence-free constraint.

This estimate is coarse but finite and explicit.

## 7. Nonlocal gradient-vorticity count

The nonlocal term contains one inverse derivative through Biot--Savart and multiplication by `grad Omega`.

Schematically it has order `-1` relative to vorticity:

\[
K_{\nabla\Omega}
\sim
M_{\nabla\Omega}\,|\nabla|^{-1}
+
\text{adjoint/lower-order variants}.
\]

On a fixed compact core with smooth coefficients this is compact.

Standard Cwikel/Schatten scaling for an order `-1` operator in dimension three suggests the weak-Schatten `S_3` count

\[
\boxed{
N_{nl}(\Lambda;R)
\lesssim
\Lambda^{-3}
\|\nabla\Omega\|_{L^3(B_R)}^3
}
\]

up to the constants attached to the precise Biot--Savart matrix operator and the retained function space.

For M19 bookkeeping, this should be read as the natural quantitative target; the exact connector-independent constant is not claimed here.

## 8. Combined superthreshold count

After choosing `R` so that the tail form contributes less than a fixed fraction of `Lambda_1`, a schematic count for channels above `Lambda_1` is

\[
\boxed{
N_+(\Lambda_1)
\le
N_{strain}(c\Lambda_1;R)
+
N_{nl}(c\Lambda_1;R),
}
\]

with `0<c<1` absorbing the tail/form decomposition.

Hence nonsymmetry kernel rigidity follows if one can prove

\[
\boxed{
N_{strain}(c\Lambda_1;R)
+
N_{nl}(c\Lambda_1;R)
\le
 d_0.
}
\]

This is now a finite compact-core quantitative inequality.

## 9. What is gained

The live kernel problem has moved through the chain

\[
\text{infinite PDE spectrum}
\to
\text{finite hard fiber}
\to
\text{finite Hermitian matrix}
\to
\text{finite compact-core superthreshold eigenchannel count}.
\]

The far critical tail cannot supply additional above-threshold channels.

Thus any failure of kernel rigidity is forced into a finite core where it must be supported by sufficiently strong strain and/or gradient-vorticity coupling.

## 10. What is not yet gained

The current project bounds do not yet show that the finite-core count is at most the exact symmetry multiplicity `d_0`.

In particular, the coarse quantity

\[
R^3
\left(
\frac{M_S(R)}{\nu}
\right)^{3/2}
\]

may be much larger than `d_0`.

Therefore no kernel contradiction is claimed.

## 11. Audit verdict

### Proved structurally

1. Every superthreshold compensation channel is localized to a finite compact core.
2. The `r^-2` critical strain tail is CLR-borderline for unthresholded global counting.
3. The strict positive threshold removes the far-tail count problem because the background coefficient itself tends to zero.
4. The remaining kernel problem is a finite-core eigenchannel-count problem.

### Conditional quantitative target

A rigorous implementation of the nonlocal Schatten count should use the precise Biot--Savart operator and chosen hard Hilbert space. The exponent `3` is the natural dimension/order scaling, but no universal sharp constant is asserted in this module.

## 12. Next target

M19-162 should test whether the **background equations themselves** constrain the finite-core superthreshold count more strongly than the coarse Weyl/CLR estimate.

The first candidate is a trace/Ky-Fan identity comparing the compensation trace on the hard fiber with the background enstrophy production

\[
\int\Omega\cdot S_U\Omega,
\]

and asking whether the exact time/rotation symmetry block already exhausts the available positive trace budget.
