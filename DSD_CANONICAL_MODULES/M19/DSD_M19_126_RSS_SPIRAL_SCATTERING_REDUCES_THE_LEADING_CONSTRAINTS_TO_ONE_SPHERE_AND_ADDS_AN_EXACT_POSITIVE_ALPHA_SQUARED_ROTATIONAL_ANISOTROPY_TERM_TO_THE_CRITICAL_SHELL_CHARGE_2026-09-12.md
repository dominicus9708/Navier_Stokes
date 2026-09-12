# DSD M19-126 — RSS spiral scattering reduces the leading constraints to one sphere and adds an exact positive alpha^2 rotational-anisotropy term to the critical shell charge

Date: 2026-09-12

Status: **ACTIVE M19 CALCULATION / M19-125 SPIRAL LAW INSERTED INTO DIVERGENCE, PRESSURE, AND CRITICAL DIRICHLET SHELL GEOMETRY / NONAXISYMMETRIC RSS TAILS PAY AN EXACT POSITIVE ROTATIONAL-ANISOTROPY CONTRIBUTION PROPORTIONAL TO ALPHA^2 / LEADING PRESSURE REMAINS SOLVABLE RATHER THAN PROVIDING A LIOUVILLE OBSTRUCTION / GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. RSS scattering spiral

M19-125 gives

\[
\boxed{
A(q)=e^{-2\alpha q\mathcal R_\omega}A_0,
\qquad
\partial_qA=-2\alpha\mathcal R_\omega A.
}
\]

Rotation preserves radial/tangential decomposition and all rotation-invariant sphere norms.

Hence it is enough to study one reference angular profile

\[
A_0(\omega).
\]

---

## 2. Divergence-free condition becomes one sphere equation

Write

\[
A=A_r\omega+A_T,
\qquad
A_T\cdot\omega=0.
\]

The general critical divergence constraint is

\[
\partial_qA_r+A_r+\operatorname{div}_{S^2}A_T=0.
\]

For RSS,

\[
\partial_qA_r=-2\alpha\mathcal R_\omega^{sc}A_r,
\]

where `R_omega^sc` is the scalar angular Lie derivative around the rotation axis.

Thus the entire q-family is divergence-free iff the reference sphere data satisfy

\[
\boxed{
-2\alpha\mathcal R_\omega^{sc}A_{0,r}
+A_{0,r}
+\operatorname{div}_{S^2}A_{0,T}
=0.
}
\]

This is a single angular first-order constraint.

---

## 3. Toroidal spiral modes remain admissible at leading order

If

\[
A_{0,r}=0,
\qquad
\operatorname{div}_{S^2}A_{0,T}=0,
\]

then the divergence constraint is automatically satisfied for every `alpha`.

Hence pure toroidal nonaxisymmetric spiral data survive the leading incompressibility test.

Therefore

\[
\boxed{
\text{RSS spiral covariance + divergence free}
\not\Rightarrow A=0.
}
\]

This blocks another possible leading-order shortcut.

---

## 4. Leading pressure equation in the spiral class

The general critical pressure equation is

\[
-\left(
\partial_q^2-3\partial_q+2+\Delta_{S^2}
\right)\Pi
=F[A].
\]

Rotation equivariance of the quadratic pressure source implies that an RSS spiral source has the same group covariance. Seek

\[
\Pi(q)=e^{-2\alpha q\mathcal R_\omega^{sc}}\Pi_0.
\]

Then

\[
\partial_q\Pi=-2\alpha\mathcal R_\omega^{sc}\Pi,
\qquad
\partial_q^2\Pi=4\alpha^2(\mathcal R_\omega^{sc})^2\Pi.
\]

Thus `Pi_0` solves the sphere equation

\[
\boxed{
-\left[
4\alpha^2(\mathcal R_\omega^{sc})^2
+6\alpha\mathcal R_\omega^{sc}
+2+\Delta_{S^2}
\right]\Pi_0
=F[A_0].
}
\]

---

## 5. Nonaxisymmetric pressure modes have no real-alpha neutral root

On a scalar spherical harmonic with azimuthal number `m`,

\[
\mathcal R_\omega^{sc}=im,
\qquad
\Delta_{S^2}=-\ell(\ell+1).
\]

The homogeneous multiplier inside the bracket is

\[
\boxed{
-4\alpha^2m^2
+6i\alpha m
+2-\ell(\ell+1).
}
\]

For real nonzero `alpha` and nonzero `m`, the imaginary part is

\[
6\alpha m\ne0,
\]

so this multiplier cannot vanish.

Therefore the leading RSS pressure problem is invertible on every genuinely nonaxisymmetric scalar harmonic.

The familiar neutral pressure root can only survive in the axisymmetric `m=0` sector, where the operator reduces to the previously known angular harmonic degeneracy.

Hence

\[
\boxed{
\text{nonaxisymmetric RSS rotation removes, rather than creates, the leading pressure resonance.}
}

This improves solvability but does not produce a Liouville contradiction.

---

## 6. Critical shell Dirichlet density

For

\[
U(r,\omega,s)
=r^{-1}A(q,\omega)+O(r^{-3}),
\qquad
q=\log r-s/2,
\]

the leading radial derivative is

\[
\partial_rU
=r^{-2}(\partial_qA-A)+O(r^{-4}).
\]

Angular derivatives contribute

\[
r^{-2}\nabla_{S^2}A.
\]

Thus on a fixed-ratio annulus

\[
R<r<\Lambda R,
\]

the weighted Dirichlet shell charge has leading form

\[
\boxed{
J_R
:=R\int_{A_R}|\nabla U|^2dy
\sim
C_{\Lambda}
\int_{I_q}
\left(
|\partial_qA-A|^2
+|\nabla_{S^2}A|^2
\right)dq\,d\omega,
}
\]

up to the standard tensorial spherical-coordinate equivalence constants and the `O(r^-3)` correction.

For RSS the integrand is q-translation/rotation invariant, so its sphere integral is constant in `q`.

---

## 7. Exact alpha-squared anisotropy contribution

Insert

\[
\partial_qA=-2\alpha\mathcal R_\omega A.
\]

Then

\[
\partial_qA-A
=-(A+2\alpha\mathcal R_\omega A).
\]

The angular rotation generator is skew-adjoint in sphere `L2`, so

\[
\langle A,\mathcal R_\omega A\rangle_{S^2}=0.
\]

Therefore

\[
\boxed{
\|\partial_qA-A\|_{L^2(S^2)}^2
=
\|A\|_2^2
+4\alpha^2\|\mathcal R_\omega A\|_2^2.
}
\]

Hence the RSS critical shell charge contains the exact positive term

\[
\boxed{
4\alpha^2\|\mathcal R_\omega A_0\|_{L^2(S^2)}^2.
}
\]

In particular, for a genuinely nonaxisymmetric tail,

\[
\mathcal R_\omega A_0\ne0,
\]

large rotation rate necessarily increases the leading shell-gradient charge quadratically unless the angular profile simultaneously approaches axisymmetry.

---

## 8. Quantitative consequence under a shell-charge ceiling

If the retained Type-I/spectator corridor supplies a uniform critical-shell bound

\[
J_R\le J_*<\infty,
\]

then the leading asymptotic formula gives

\[
\boxed{
|\alpha|\,\|\mathcal R_\omega A_0\|_2
\lesssim
J_*^{1/2}.
}
\]

This is the far-field scattering analogue of the interior compensation upper bounds in M19-108 and M19-115.

Thus the tendency toward axisymmetry at large `|alpha|` is visible directly in the critical tail geometry.

---

## 9. No contradiction in the moderate band

For bounded moderate `alpha`, the positive shell contribution is finite and perfectly compatible with the critical `1/r` tail.

Hence

\[
\boxed{
\text{spiral shell charge}
\text{ narrows the RSS tail but does not eliminate the moderate branch.}
}

The pressure inversion is likewise regular in nonaxisymmetric modes.

Therefore the moderate Liouville obstruction must come from a deeper matching of:

- compact-core torque/adjoint identities;
- critical spiral tail;
- or global nonlinear structure.

---

## 10. Next target

The natural next calculation is to compare the **interior rotational defect**

\[
\|\mathcal RU\|_{L^2_\mu}
\]

in the Pineau--Vicol compensation band with the **far-field angular defect**

\[
\|\mathcal R_\omega A_0\|_{L^2(S^2)}.
\]

A quantitative tail-to-core observability inequality relating these two quantities would turn the separate interior and far-field compensation laws into one global rigidity condition.

No such inequality is currently certified.

---

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
