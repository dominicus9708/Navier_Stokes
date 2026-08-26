# DSD M5-12 — Scalar Joint-Boundary Pressure-Cancellation No-Go

Date: 2026-08-26

Status: **DERIVED ALGEBRAIC NO-GO INSIDE THE SCALAR ISOTROPIC MULTIPLIER CLASS / THIS DOES NOT RULE OUT NONLOCAL, VECTORIAL, VORTICITY-BASED, OR SOLUTION-SPECIFIC CANCELLATIONS / GLOBAL REGULARITY UNPROVED.**

## 1. Goal

M5-12 asked whether the exact amplitude-boundary ledger `K` and the exact spatial weighted-energy ledger could be combined on the joint projective boundary `lambda r ~ 1` so that the pressure source cancels exactly.

Rather than guess coefficients, consider the general scalar isotropic functional

\[
\mathcal L_\Phi[U]
:=\int_{\mathbb R^3}\Phi(Y,a)\,dY,
\qquad a=|U|.
\]

Assume enough smoothness/decay for the formal calculation; nonsmooth truncations are recovered by approximation.

## 2. Exact pressure contribution

Let

\[
n=U/a,
\qquad
q(Y,a):=\frac{\partial_a\Phi(Y,a)}{a}.
\]

Because the Leray/physical momentum equation contains `+ grad P`, the pressure contribution to `d L_Phi / dt` or to the corresponding Leray-time derivative is

\[
-\int \partial_a\Phi\,n\cdot\nabla P\,dY
=-\int qU\cdot\nabla P\,dY.
\]

Using `div U=0`,

\[
\boxed{
\mathcal P_\Phi
=\int P\,\operatorname{div}(qU)\,dY
=\int P\,U\cdot\nabla q\,dY.
}
\]

Thus scalar localization creates pressure work precisely through variation of the multiplier `q` along incompressible streamlines.

## 3. Algebraic pressure-neutrality

If pressure is to disappear **by incompressibility alone**, without using a special solution-dependent pressure identity, it is enough and, within this multiplier mechanism, necessary to require

\[
U\cdot\nabla q\equiv0
\]

for every admissible divergence-free field.

Universal algebraic neutrality therefore forces

\[
q\equiv c,
\]

so

\[
\partial_a\Phi=ca
\]

and hence

\[
\boxed{
\Phi(Y,a)=\frac c2a^2+C(Y).
}
\]

The term `C(Y)` is independent of the velocity and does not produce a new Navier--Stokes state functional.

Therefore the only universally pressure-neutral member of this scalar isotropic multiplier class is the ordinary quadratic kinetic-energy density, up to irrelevant additive spatial terms.

## 4. Recovery of the known ledgers

### Amplitude threshold

For

\[
\Phi_K(a)=\frac\lambda2(a^2-\lambda^2)_+,
\]

one has

\[
q_K=\lambda\mathbf 1_{\{a>\lambda\}},
\]

whose streamline derivative is a level-set distribution. This produces the amplitude pressure flux `lambda J_P(lambda)`.

### Spatial weighted energy

For

\[
\Phi_W(Y,a)=\frac{a^2}{2|Y|},
\]

one has

\[
q_W=|Y|^{-1},
\]

and therefore

\[
\mathcal P_W
=\int P U\cdot\nabla |Y|^{-1}\,dY,
\]

which is exactly the critical radial pressure-flux term.

Any finite linear combination of these retains a nonconstant `q` and therefore retains a pressure source.

## 5. Joint projective multipliers

Let

\[
z:=a|Y|
\]

be the scale-invariant joint amplitude-radius coordinate. A general joint multiplier `q=q(z)` gives

\[
\boxed{
\mathcal P_q
=\int P q'(z) U\cdot\nabla z\,dY.
}
\]

Thus the remaining source is the **projective streamline defect**

\[
\boxed{
\Xi:=U\cdot\nabla(|Y||U|)
=|Y|\,U\cdot\nabla|U|+|U|\,U\cdot\nabla|Y|.
}
\]

A nonconstant joint multiplier is pressure-neutral on a particular flow only if an additional solution-specific cancellation occurs; the strongest pointwise locking is `Xi=0`.

In log-spherical variables `F=|Y|U`, this is exactly transport of the projective amplitude `|F|` along the velocity field.

## 6. DSD interpretation

The amplitude boundary and spatial boundary are not two pressure sources that can generically be assigned opposite coefficients and cancelled. They are two manifestations of the same rule:

\[
\boxed{
\text{scalar localization}
\Longrightarrow
\text{multiplier variation along streamlines}
\Longrightarrow
\text{pressure work}.
}
\]

The only scalar isotropic localization that removes this mechanism universally is no localization at all: ordinary kinetic energy.

Hence M5 cannot be closed by a scalar `K + weighted-energy` cancellation trick.

## 7. What this does and does not prove

This result rules out only **universal algebraic pressure cancellation inside scalar isotropic velocity-magnitude/spatial-weight functionals**.

It does **not** rule out:

- nonlocal Hodge-projected critical functionals;
- vorticity/helicity functionals;
- tensorial or directional multipliers;
- cancellations using the pressure Poisson equation;
- cancellations specific to a restricted W1 geometry.

Therefore the next candidate class should be pressure-free by divergence-free projection rather than by scalar localization.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
