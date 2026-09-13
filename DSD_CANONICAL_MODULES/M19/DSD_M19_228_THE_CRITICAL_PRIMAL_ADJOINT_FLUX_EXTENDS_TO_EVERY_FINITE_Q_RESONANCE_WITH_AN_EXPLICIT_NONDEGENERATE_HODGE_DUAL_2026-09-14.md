# M19-228 — The critical primal–adjoint flux extends to every finite q resonance with an explicit nondegenerate Hodge dual

**Date:** 2026-09-14  
**Status:** ACTIVE CALCULATION / ALL-RESONANCE DUAL-FLUX UNIFICATION

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-224--227 focused on the zero-q branch. M19-216 had separately reduced the nonzero-q bounded-period branch to finitely many resonances.

This module shows that the same physical adjoint critical flux applies to every real q-frequency kappa. At the angular level the primal and adjoint divergence constraints admit an explicit nondegenerate Hermitian dual pairing.

Thus the zero-q and finite nonzero-q bounded-period kernel branches have one common Fredholm boundary form.

## 2. Primal and adjoint critical modes at frequency kappa

Take a complexified primal critical mode

\[
\boxed{
W
=
r^{-1}e^{i\kappa q}b(\omega)+O(r^{-3}),
\qquad
q=\log r-\frac s2,
}
\]

and an adjoint critical mode with the same q-frequency

\[
\boxed{
\Psi
=
r^{-2}e^{i\kappa q}c(\omega)+O(r^{-4}).
}
\]

Use the Hermitian L2 pairing W dot conjugate(Psi). Then the q phases cancel:

\[
e^{i\kappa q}\overline{e^{i\kappa q}}=1.
\]

The M19-225 Green-current calculation therefore gives

\[
\boxed{
\lim_{R\to\infty}\mathcal F_R
=
-\frac12
\langle b,c\rangle_{L^2(S^2;\mathbb C^3)}.
}
\]

All diffusion/background/pressure contributions remain O(R^-2).

## 3. Primal angular divergence constraint

Write

\[
b=b_r\omega+b_T,
\qquad
b_T=\nabla_{S^2}\phi+\omega\times\nabla_{S^2}\psi.
\]

The primal r^-1 divergence constraint is

\[
(i\kappa+1)b_r+\operatorname{div}_{S^2}b_T=0.
\]

Hence

\[
\boxed{
\Delta_{S^2}\phi
=-(1+i\kappa)b_r,
\qquad
\phi=-(1+i\kappa)\Delta_{S^2}^{-1}b_r.
}
\]

For kappa nonzero, integrating the constraint also forces the spherical mean of b_r to vanish. At kappa=0 the same mean-zero condition is already inherited from the recurrent zero-flux branch.

## 4. Adjoint angular divergence constraint

Write

\[
c=c_r\omega+c_T,
\qquad
c_T=\nabla_{S^2}\chi+\omega\times\nabla_{S^2}\zeta.
\]

At the adjoint critical exponent r^-2,

\[
\partial_qC_r+\operatorname{div}_{S^2}C_T=0.
\]

For frequency kappa this becomes

\[
\boxed{
i\kappa c_r+\Delta_{S^2}\chi=0,
}
\]

so

\[
\boxed{
\chi=-i\kappa\Delta_{S^2}^{-1}c_r.
}
\]

The toroidal scalar zeta is independent.

## 5. Explicit dual datum

Given a nonzero primal datum b with radial scalar b_r and toroidal scalar psi, define the adjoint angular datum c_b by

\[
\boxed{
(c_b)_r=b_r,
\qquad
\chi_b=-i\kappa\Delta_{S^2}^{-1}b_r,
\qquad
\zeta_b=\psi.
}
\]

Thus

\[
\boxed{
 c_b
=
 b_r\omega
+\nabla_{S^2}\bigl(-i\kappa\Delta_{S^2}^{-1}b_r\bigr)
+\omega\times\nabla_{S^2}\psi.
}
\]

By construction c_b satisfies the adjoint divergence constraint.

## 6. The Hermitian pairing has strictly positive real part

Expand b_r in spherical harmonics with positive eigenvalues

\[
-\Delta_{S^2}Y_{\ell m}
=\lambda_\ell Y_{\ell m},
\qquad
\lambda_\ell=\ell(\ell+1)>0.
\]

On one radial harmonic coefficient a_{\ell m}, the primal poloidal potential has coefficient

\[
\frac{1+i\kappa}{\lambda_\ell}a_{\ell m},
\]

while the adjoint poloidal potential has coefficient

\[
\frac{i\kappa}{\lambda_\ell}a_{\ell m}.
\]

The radial plus poloidal contribution to the Hermitian pairing is therefore

\[
|a_{\ell m}|^2
\left[
1+
\frac{\kappa^2-i\kappa}{\lambda_\ell}
\right].
\]

Hence

\[
\boxed{
\operatorname{Re}\langle b,c_b\rangle
=
\sum_{\ell,m}
\left(1+\frac{\kappa^2}{\lambda_\ell}\right)
|a_{\ell m}|^2
+
\|\nabla_{S^2}\psi\|_2^2
>0
}
\]

for every nonzero b.

Thus the angular primal/adjoint critical spaces are nondegenerately paired at every real kappa.

For kappa=0 this reduces to M19-225:

\[
\operatorname{Re}\langle b,c_b\rangle
=
\|b_r\|_2^2+\|\nabla\psi\|_2^2.
\]

## 7. Compatibility with RDSS holonomy

Suppose the primal angular datum belongs to a holonomy eigenspace

\[
Q_*^{-1}b=e^{i\phi}b.
\]

The sphere Hodge operators, Delta^{-1}, gradient, and toroidal curl commute with physical rotations. Therefore c_b lies in the same holonomy representation sector:

\[
\boxed{
Q_*^{-1}c_b=e^{i\phi}c_b.
}
\]

If the primal kernel resonance is

\[
\boxed{
\kappa L-\phi=2\pi n,
}
\]

then the adjoint critical datum constructed above obeys the same relative-periodic phase matching.

Hence there is no additional angular/holonomy obstruction to the dual mode.

## 8. Period-integrated Green compatibility for every resonance

If a global smooth relative-periodic physical adjoint realization of c_b exists, the M19-225 period integration yields

\[
0
=
-\frac S2
\langle b,c_b\rangle.
\]

Taking real parts gives

\[
0
=
-\frac S2
\operatorname{Re}\langle b,c_b\rangle,
\]

contradicting the strict positivity above for b nonzero.

As in M19-226, this is a conditional Fredholm contradiction and cannot be converted into an unconditional proof by assuming arbitrary adjoint critical-data surjectivity.

## 9. Structural unification of the bounded-period kernel frontier

M19-216--217 split the residual bounded-period theorem into

\[
\mathcal T_{q0}^{lin}
\cup
\mathcal T_{q\ne0}^{fin-res}.
\]

M19-228 shows that at the primal-adjoint critical boundary-form level both are instances of one problem:

\[
\boxed{
\mathcal T_{res}^{int-adj}:
\text{classify which nondegenerate critical dual functionals extend through the finite spectator boundary/interior relative-periodic problem.}
}
\]

The q-frequency changes the angular dual formula but not the Fredholm architecture.

Thus the old q=0 versus q-not-zero split remains useful for direct primal calculations, but is no longer fundamental for the adjoint-flux formulation.

## 10. Certified / not certified

### Certified

1. The r^-1/r^-2 critical Green flux works at every real q-frequency.
2. The primal and adjoint angular divergence constraints can be solved explicitly by spherical Hodge decomposition.
3. Every nonzero primal angular datum has an explicit adjoint critical datum with strictly positive real Hermitian pairing.
4. The construction respects physical rotation holonomy.
5. Every bounded-period finite resonance therefore has the same conditional dual-flux contradiction.

### Not certified

1. Global relative-periodic realization of the prescribed adjoint critical datum.
2. A noncircular theorem forcing such realization.
3. Bounded-period kernel exclusion.
4. Aperiodic signed-invariant closure.
5. Global regularity.

## 11. Next target

Use M19-227 to pull the explicit dual functional to a sufficiently remote finite spectator boundary, then formulate the remaining interior extension problem as a finite-boundary relative-periodic parabolic Fredholm/trace problem. Audit whether its obstruction is strictly smaller than the original whole-space kernel problem or merely another equivalent formulation.
