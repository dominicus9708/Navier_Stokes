# Exact Global Covariance Deficit Identity — 2026-08-20

Overall status: **EXACT WHOLE-SPACE COMPATIBILITY IDENTITY — GLOBAL REGULARITY NOT PROVED.**

This note identifies the exact positive quantities behind the global compatibility cap

\[
\lambda_{max}(\mathbb C)\le\frac23.
\]

---

## 1. Fixed-axis covariance numerator

Fix a constant unit vector `n`. Let

\[
P=\|\nabla S\|_2^2.
\]

Define

\[
I_n
=
\|\partial_nS\|_2^2
+2\sum_k\|(\partial_kS)n\|_2^2.
\]

Then

\[
\boxed{
n^T\mathbb Cn=\frac{I_n}{3P}.}
\]

The global `2/3` cap is equivalent to

\[
I_n\le2P.
\]

---

## 2. Fourier decomposition of the deficit

For each nonzero frequency write

\[
\widehat k=k/|k|,
\qquad
\widehat a=\widehat u/|\widehat u|,
\qquad
\widehat a\perp\widehat k.
\]

Complete this to an orthonormal frame

\[
(\widehat k,\widehat a,\widehat b),
\qquad
\widehat b=\widehat k\times\widehat a.
\]

Resolve `n` as

\[
n=c\widehat k+d\widehat a+e\widehat b,
\qquad
c^2+d^2+e^2=1.
\]

For a compatible strain mode,

\[
\widehat S
=\frac i2(k\otimes\widehat u+\widehat u\otimes k).
\]

The mode contribution to `P` is

\[
P_k
=|k|^2|\widehat S|^2
=\frac12|k|^4|\widehat u|^2.
\]

The fixed-axis covariance numerator satisfies

\[
(I_n)_k
=(2c^2+d^2)P_k.
\]

Therefore

\[
2P_k-(I_n)_k
=(d^2+2e^2)P_k.
\]

---

## 3. Identify the two physical-space positive terms

Since

\[
d=\frac{n\cdot\widehat u}{|\widehat u|},
\]

we have

\[
d^2P_k
=\frac12|k|^4|n\cdot\widehat u|^2.
\]

Also

\[
\widehat\omega
=ik\times\widehat u
=i|k||\widehat u|\widehat b,
\]

so

\[
2e^2P_k
=|k|^2|n\cdot\widehat\omega|^2.
\]

Summing over frequencies and applying Parseval gives the exact identity

\[
\boxed{
2P-I_n
=
\frac12\|\Delta(u\cdot n)\|_2^2
+\|\nabla(\omega\cdot n)\|_2^2.
}
\]

Both terms are nonnegative.

---

## 4. Exact covariance defect formula

Because

\[
\frac23-n^T\mathbb Cn
=\frac{2P-I_n}{3P},
\]

we obtain

\[
\boxed{
\frac23-n^T\mathbb Cn
=
\frac{\|\Delta(u\cdot n)\|_2^2}{6P}
+
\frac{\|\nabla(\omega\cdot n)\|_2^2}{3P}.
}
\]

Thus the compatibility tax has a direct physical meaning.

A profile can approach the `2/3` fixed-axis covariance ceiling only if it simultaneously makes

\[
\Delta(u\cdot n)
\to0
\]

and

\[
\nabla(\omega\cdot n)
\to0
\]

relative to the strain-gradient scale.

---

## 5. Equality rigidity

If equality

\[
n^T\mathbb Cn=\frac23
\]

holds for a finite-energy whole-space profile, then

\[
\Delta(u\cdot n)=0
\]

in `L2`, and

\[
\nabla(\omega\cdot n)=0
\]

in `L2`.

Whole-space decay then forces

\[
u\cdot n=0,
\qquad
\omega\cdot n=0.
\]

The Fourier derivation further shows that all active frequencies must be parallel to `n`, which is incompatible with a nonzero `L2(R^3)` Fourier transform. Hence exact equality is trivial.

---

## 6. Relation to the recurrent P_V branch

The old pointwise `7/9` near-saturation geometry wanted a nearly fixed compressive axis and almost one-dimensional derivative structure.

The exact whole-space compatibility identity shows that even after such an axis is selected, approaching the improved `2/3` ceiling imposes two further costs:

1. axial velocity curvature depletion;
2. axial vorticity-gradient depletion.

Failure of either depletion produces an explicit fixed-axis covariance defect.

This gives new quantities that can be tested against the first-hitting vorticity cap, the non-normality identity, and the existing `H/T` derivative reservoirs.

---

## 7. Localization target

For a cutoff `chi_R`, applying the whole-space identity to a divergence-free localization of `u` will reproduce the same positive core terms plus commutator/boundary errors supported in the annulus.

Thus the correct local version is expected to have the schematic form

\[
I_{n,B_R}
\le
2P_{B_{2R}}
-
\frac12\|\Delta(u\cdot n)\|_{B_R}^2
-
\|\nabla(\omega\cdot n)\|_{B_R}^2
+
\mathcal E_{ann}(R),
\]

where `E_ann` is a localization/turnover cost. Deriving this annular error with explicit constants is the next localization step.

Status: **THE GLOBAL `2/3` COVARIANCE CAP IS THE CONSEQUENCE OF AN EXACT SUM-OF-SQUARES DEFICIT: AXIAL VELOCITY CURVATURE PLUS AXIAL VORTICITY-GRADIENT ENERGY. THIS IDENTIFIES THE PRECISE QUANTITIES THAT MUST VANISH IN ANY NEAR-SATURATING FIXED-AXIS RECURRENT PROFILE.**