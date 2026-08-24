# DSD RSS Two-Level Rotational Phase Consistency

Date: 2026-08-25

Status: **H0 AND H1 ROTATION-GENERATOR IDENTITIES DERIVED WITH THE SAME ALPHA / EXACT CROSS-LEVEL PHASE-CONSISTENCY CONDITION OBTAINED / FINITE TWO-LEVEL RSS EXCLUSION TEST CREATED / GLOBAL REGULARITY UNPROVED.**

## 1. Purpose

The H0/H1 scalar recurrence balances are blind to the RSS rotation speed because they use rotation-invariant norms.

The rotation-generator pairing at the vorticity `L2` level restores the angular phase channel:

\[
\alpha A_0+\frac12I_0+B_0=0.
\]

A genuine constant-rate RSS orbit must produce **the same angular speed `alpha` at every Sobolev level**.

This note derives the first finite cross-level compatibility test by repeating the generator pairing at vorticity H1 level.

---

## 2. H0 phase variables

Use the RSS vorticity equation

\[
\alpha\mathcal G\Omega
+\Omega
+\frac12D\Omega
+\mathcal N_\Omega
-\nu\Delta\Omega
=0.
\]

Define

\[
A_0:=\|\mathcal G\Omega\|_2^2,
\]

\[
I_0:=\langle D\Omega,\mathcal G\Omega\rangle,
\]

\[
B_0:=\langle\mathcal N_\Omega,\mathcal G\Omega\rangle.
\]

The H0 generator identity is

\[
\boxed{
\alpha A_0+\frac12I_0+B_0=0.
}
\tag{G0}
\]

If `A0>0`,

\[
\boxed{
\alpha
=-\frac{\frac12I_0+B_0}{A_0}.
}
\tag{alpha0}
\]

---

## 3. H1 angular activity

Pair the same RSS vorticity equation with

\[
-\Delta\mathcal G\Omega.
\]

Because `G` commutes with `Delta`,

\[
-\Delta\mathcal G\Omega
=\mathcal G(-\Delta\Omega).
\]

Define

\[
\boxed{
A_1
:=
\langle\mathcal G\Omega,-\Delta\mathcal G\Omega\rangle
=
\|\nabla\mathcal G\Omega\|_2^2.
}
\]

The rotation term therefore contributes

\[
\alpha A_1.
\]

---

## 4. Rotation-invariant linear terms again vanish where appropriate

For the zeroth-order term,

\[
\langle\Omega,-\Delta\mathcal G\Omega\rangle
=
\langle-\Delta\Omega,\mathcal G\Omega\rangle
=0
\]

by self-adjointness of `-Delta`, commutation, and skew-adjointness of `G`.

For the viscous term,

\[
\begin{aligned}
\langle-\nu\Delta\Omega,-\Delta\mathcal G\Omega\rangle
&=
\nu\langle\Delta\Omega,\Delta\mathcal G\Omega\rangle\\
&=0,
\end{aligned}
\]

because `G` is skew-adjoint also in the `Delta`-weighted inner product.

Thus viscosity again does not directly see rigid rotation speed.

---

## 5. H1 rotation-dilation and nonlinear phase channels

Define

\[
\boxed{
I_1
:=
\langle D\Omega,-\Delta\mathcal G\Omega\rangle
=
\langle\nabla D\Omega,\nabla\mathcal G\Omega\rangle,
}
\]

and

\[
\boxed{
B_1
:=
\langle\mathcal N_\Omega,-\Delta\mathcal G\Omega\rangle.
}
\]

The H1 generator pairing gives

\[
\boxed{
\alpha A_1+\frac12I_1+B_1=0.
}
\tag{G1}
\]

Hence, if `A1>0`,

\[
\boxed{
\alpha
=-\frac{\frac12I_1+B_1}{A_1}.
}
\tag{alpha1}
\]

---

## 6. Exact two-level phase consistency

A single RSS profile has one and only one constant angular speed `alpha`.

Equating (alpha0) and (alpha1) yields

\[
\boxed{
\frac{\frac12I_0+B_0}{A_0}
=
\frac{\frac12I_1+B_1}{A_1}.
}
\]

Equivalently,

\[
\boxed{
A_1\left(\frac12I_0+B_0\right)
-
A_0\left(\frac12I_1+B_1\right)
=0.
}
\tag{2L}
\]

This is an exact finite two-level rotation-phase compatibility condition.

It is independent of `alpha` after elimination.

---

## 7. Direct exclusion test

Define the phase quotients

\[
\boxed{
\Xi_0
:=
-\frac{\frac12I_0+B_0}{A_0},
\qquad
\Xi_1
:=
-\frac{\frac12I_1+B_1}{A_1}.
}
\]

Every genuinely rotation-active RSS profile with finite channels must satisfy

\[
\boxed{
\Xi_0=\Xi_1=\alpha.
}
\]

Therefore any class estimate producing a strict separation

\[
\boxed{
|\Xi_0-\Xi_1|\ge\delta_{01}>0
}
\]

excludes exact RSS in that class.

This provides a new target qualitatively different from trying to prove `alpha` small or large directly.

---

## 8. Homogeneous critical tail is neutral at both levels

For an exactly `-2` homogeneous vorticity tail,

\[
D\Omega=-2\Omega.
\]

Then

\[
I_0=-2\langle\Omega,\mathcal G\Omega\rangle=0.
\]

Moreover

\[
\nabla(D\Omega)=-2\nabla\Omega,
\]

so

\[
I_1
=-2
\langle\nabla\Omega,\nabla\mathcal G\Omega\rangle
=0
\]

by H1 skew-adjointness of the rotation generator.

Thus a perfectly homogeneous passive critical tail does not create a mismatch between `Xi0` and `Xi1` through the dilation channels.

Any nontrivial two-level phase mismatch must come from the active core, core-tail transition, radial modulation, or nonlinear angular transfers `B0,B1`.

---

## 9. Relation to the H0/H1 scalar recurrence taxes

The scalar recurrence identities constrain

\[
\frac14Z+\nu Q=\mathcal P_0
\]

and

\[
\frac38Q+\frac\nu2R=N_1
\]

on an RSS orbit.

Those equations determine the required **radial/spectral production magnitudes** but not their angular phase.

The new identity (2L) requires that the angular phase transfers at the two levels organize themselves around one common `alpha`.

Thus a future closure may combine:

- scalar production floors from H0/H1;
- algebraic incompatibility/non-normality gaps;
- the two-level angular phase consistency `Xi0=Xi1`.

This is the first finite route that can potentially make the old H0/H1 taxes relevant to the intermediate-rotation problem without pretending they contain `alpha` directly.

---

## 10. Scope warning

The H1 generator channel requires enough regularity that

\[
\nabla\mathcal G\Omega\in L^2
\]

and the nonlinear pairing `B1` is finite.

This is stronger than bare weak-L3 velocity tail information and must be verified on any candidate class before using (G1).

On smooth Type-I RSS profiles with the expected `1/R`, `1/R^2`, and derivative decays, the formal far-field scaling is compatible with these integrals, but the proof route must retain the explicit regularity assumption or establish it by the annular H2/Higher-tail ledger.

---

## 11. DSD audit

Two distinct phase layers are formed:

- H0 angular activity/transfer: `A0,I0,B0`;
- H1 angular activity/transfer: `A1,I1,B1`.

Only after both layers are formed is the common physical parameter `alpha` eliminated.

No infinite Sobolev hierarchy is invoked; this is a finite two-level composition.

---

## 12. Updated RSS frontier

A surviving exact RSS must now satisfy simultaneously:

\[
\boxed{
\begin{aligned}
&\text{H0/H1 scalar recurrence taxes},\\
&\text{rotation-dilation discriminant }B_0^2+2A_0C_0\ge0,\\
&\text{Pineau-Vicol rotational speed payment},\\
&\text{two-level phase consistency }\Xi_0=\Xi_1.
\end{aligned}
}
\]

The next calculation should attempt to estimate `B0` and `B1` using the same strain/vorticity covariance tensors already developed for the H0/H1 production-gap analysis, rather than introducing additional derivative levels.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
