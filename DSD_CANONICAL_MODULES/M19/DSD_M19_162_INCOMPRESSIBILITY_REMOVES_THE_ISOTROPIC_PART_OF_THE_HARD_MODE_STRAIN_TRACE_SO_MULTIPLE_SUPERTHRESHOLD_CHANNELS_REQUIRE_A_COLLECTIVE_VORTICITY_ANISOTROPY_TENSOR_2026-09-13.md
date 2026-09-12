# DSD M19-162 — Incompressibility removes the isotropic part of the hard-mode strain trace, so multiple superthreshold channels require a collective vorticity anisotropy tensor

**Date:** 2026-09-13  
**Status:** ACTIVE M19 CALCULATION / TRACE-ANISOTROPY REDUCTION / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Purpose

M19-161 localized every superthreshold compensation channel to a finite compact core.
The next question is whether the background equations constrain the **number** of such channels more strongly than a coarse finite-volume eigenvalue count.

The first exact gain comes from incompressibility at the level of the collective hard-mode density tensor.

## 2. Hard-mode collective density tensor

At a fixed similarity time choose an `L2`-orthonormal family of hard vorticity perturbations

\[
\eta_1,\ldots,\eta_m.
\]

Define the matrix-valued density

\[
\boxed{
\Gamma_E(y)
:=
\sum_{j=1}^m
\eta_j(y)\otimes\eta_j(y).
}
\]

Its scalar density is

\[
\rho_E(y)
:=
\operatorname{tr}\Gamma_E(y)
=
\sum_{j=1}^m|\eta_j(y)|^2.
\]

Decompose

\[
\boxed{
\Gamma_E
=
\frac{\rho_E}{3}I
+
Q_E,
\qquad
\operatorname{tr}Q_E=0.
}
\]

Here `Q_E` is the collective vorticity-anisotropy tensor of the hard family.

## 3. Exact cancellation of the isotropic strain trace

The local strain part of the compensation trace over the family is

\[
\sum_{j=1}^m
\int
\eta_j\cdot S_U\eta_j\,dy
=
\int
S_U:\Gamma_E\,dy.
\]

Since the background is incompressible,

\[
\operatorname{tr}S_U=0.
\]

Therefore

\[
S_U:\frac{\rho_E}{3}I
=
\frac{\rho_E}{3}\operatorname{tr}S_U
=0.
\]

Hence

\[
\boxed{
\sum_{j=1}^m
\int
\eta_j\cdot S_U\eta_j\,dy
=
\int
S_U:Q_E\,dy.
}
\]

This is an exact identity.

## 4. Consequence

A large **total hard-mode density** does not by itself create a large positive strain trace.

Only anisotropic organization of the hard family contributes.

In particular, if the family is pointwise isotropic in the sense

\[
\Gamma_E(y)
=
\frac{\rho_E(y)}{3}I,
\]

then

\[
\boxed{
\sum_{j=1}^m
\int
\eta_j\cdot S_U\eta_j\,dy
=0.
}
\]

Therefore multiple high-compensation channels require a persistent collective anisotropy

\[
\boxed{Q_E\ne0.}
\]

## 5. Quantitative anisotropy bound

By Cauchy--Schwarz for matrices,

\[
|S_U:Q_E|
\le
|S_U|\,|Q_E|.
\]

Thus

\[
\boxed{
\left|
\sum_{j=1}^m
\int
\eta_j\cdot S_U\eta_j
\right|
\le
\int
|S_U|\,|Q_E|.
}
\]

The traceless tensor obeys the pointwise bound

\[
|Q_E|
\le
C\rho_E,
\]

but that estimate loses the new cancellation.

A useful dimensionless anisotropy ratio is

\[
\boxed{
\mathfrak a_E(y)
:=
\frac{|Q_E(y)|}{\rho_E(y)}
\in[0,C],
}
\]

with `a_E=0` in the isotropic case.

Then

\[
\boxed{
\left|
\sum_j
\int
\eta_j\cdot S_U\eta_j
\right|
\le
\int
|S_U|\,\mathfrak a_E\rho_E.
}
\]

Thus a trace bound below the M19-159 multiplicity threshold could follow from a quantitative decorrelation/alignment theorem controlling `a_E` on the strong-strain set.

## 6. Relation to background enstrophy production

The background enstrophy stretching is

\[
\int
\Omega\cdot S_U\Omega\,dy
=
\int
S_U:(\Omega\otimes\Omega)\,dy.
\]

This has the same algebraic form as the hard-mode strain trace, but with the rank-one tensor

\[
\Omega\otimes\Omega
\]

instead of the collective tensor `Gamma_E`.

However there is no exact identity forcing

\[
Q_E
\propto
\Omega\otimes\Omega
-
\frac{|\Omega|^2}{3}I.
\]

Hence the positive background stretching budget does **not** by itself prove that the symmetry channel exhausts the hard-mode compensation trace.

Permanent firewall:

\[
\boxed{
\text{background vorticity anisotropy}
\neq
\text{hard-mode collective anisotropy}.
}
\]

## 7. Nonlocal trace

The gradient-vorticity part from M19-160 contributes

\[
\sum_{j=1}^m
\mathcal C_{grad\Omega}[W_j].
\]

Using the constant-vorticity cancellation, this depends on `grad Omega` and bilinear densities built from `W_j,eta_j`.

Schematically it can be written as

\[
\boxed{
\int
\nabla\Omega:
\mathcal J_E(W_1,\ldots,W_m)\,dy,
}
\]

for a collective hard-mode current tensor `J_E` involving Biot--Savart.

Thus the full compensation trace depends on two collective orientation objects:

\[
\boxed{
Q_E
\quad\text{and}\quad
\mathcal J_E.
}
\]

It is not determined by the scalar density `rho_E` alone.

## 8. Spectral-count implication

Suppose `m` orthonormal hard directions all lie above the enhanced compensation threshold.

M19-159 requires a total compensation trace at least

\[
\boxed{
\operatorname{Tr}_E\overline C
\ge
m\Lambda_1
}
\]

after the appropriate period normalization by the vorticity Gram form.

The present decomposition implies that this trace must be supplied by

\[
\boxed{
\int S_U:Q_E
+
\int\nabla\Omega:\mathcal J_E.
}
\]

Therefore a many-channel kernel/neutral block forces a many-mode orientation structure in the compact core.

This is stronger than merely requiring large scalar strain or large palinstrophy.

## 9. What would close the count

Any one of the following would be sufficient in principle:

1. **collective isotropization:**
   \[
   \int |S_U|\,|Q_E|
   \text{ is too small above the exact symmetry block};
   \]

2. **alignment rank bound:** the high-strain region permits only the exact symmetry anisotropy directions;

3. **nonlocal-current cancellation:** `J_E` has a signed cancellation or trace bound controlled by the same symmetry block;

4. **combined trace bound:**
   \[
   \operatorname{Tr}(K_{comp}^+)
   <(d_0+1)\Lambda_1.
   \]

No such theorem is currently certified.

## 10. Important no-go

The identity

\[
\operatorname{tr}S_U=0
\]

removes only the isotropic part of `Gamma_E`.

It does **not** force

\[
Q_E=0.
\]

Hence incompressibility alone still does not close the kernel problem.

The precise missing information is now an orientation/anisotropy theorem rather than a scalar norm estimate.

## 11. Audit verdict

### Proved

\[
\boxed{
\operatorname{Tr}_E(\text{local strain compensation})
=
\int S_U:Q_E.
}
\]

Thus every multi-channel compensation mechanism must carry collective hard-mode anisotropy.

### Not proved

No current identity ties `Q_E` strongly enough to the background vorticity tensor or exact symmetry block to bound the number of superthreshold channels by `d_0`.

## 12. Next target

M19-163 should use the **evolution equation for the hard-mode density tensor** `Gamma_E` or its traceless part `Q_E`.

If diffusion and the similarity drift damp `Q_E` more strongly than the scalar density while strain is the only source, one may obtain a closed anisotropy balance capable of limiting the number of persistent superthreshold channels.
