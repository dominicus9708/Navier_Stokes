# DSD M5-148 — Inverse-Fuchsian Flat-Infinity Formulation

Date: 2026-08-27

Status: **P1_B REFORMULATION / SETTING `xi=z^-1=r^2` CONVERTS THE FLAT FUCHSIAN BOUNDARY INTO SUPERALGEBRAIC DECAY AT `xi=+infinity`; THE VELOCITY DIFFERENCE HAS PRINCIPAL NORMAL OPERATOR `4nu partial_xixi - partial_xi`, WHILE GENEALOGICAL, ANGULAR, AND COMMON-TAIL TRANSPORT ENTER WITH `O(xi^-1)` OR SMALLER NORMAL COEFFICIENTS / FLAT UNIQUENESS IS REDUCED TO A PERTURBED ONE-WAY DIFFUSION-DRIFT UNIQUE-CONTINUATION PROBLEM / GLOBAL REGULARITY UNPROVED.**

---

## 1. Inverse-Fuchsian coordinate

Starting from M5-136,

\[
z=r^{-2},
\]

define

\[
\boxed{
\xi:=z^{-1}=r^2.
}
\]

Then

\[
z\downarrow0
\quad\Longleftrightarrow\quad
\xi\to+\infty.
\]

The genealogical coordinate remains

\[
\eta=\log r-\frac s2.
\]

Since

\[
z\partial_z=-\xi\partial_\xi,
\]

the radial operator becomes

\[
\boxed{
D=\partial_\eta+2\xi\partial_\xi.
}
\]

---

## 2. Exact transformed viscous operator

For a field `H(xi,eta,theta)`,

\[
D^2-D
=
\partial_\eta^2-\partial_\eta
+4\xi\partial_{\eta\xi}
+4\xi^2\partial_{\xi\xi}
+2\xi\partial_\xi.
\]

Also

\[
H_z=-\xi^2H_\xi.
\]

Insert these into the M5-136 equation

\[
H_z
=-\nu(D^2-D+\Delta_{S^2})H
+\mathcal B_D(H)
+\mathcal P_D(\Pi),
\]

where

\[
\mathcal P_D(\Pi)
:=\theta(D\Pi-2\Pi)+\nabla_{S^2}\Pi.
\]

After division by `xi^2`, obtain the exact form

\[
\boxed{
\begin{aligned}
0={}&4\nu H_{\xi\xi}-H_\xi
+\frac{4\nu}{\xi}H_{\eta\xi}
+\frac{2\nu}{\xi}H_\xi\\
&+\frac{\nu}{\xi^2}
(\partial_\eta^2-\partial_\eta+\Delta_{S^2})H
-\frac1{\xi^2}\mathcal B_D(H)
-\frac1{\xi^2}\mathcal P_D(\Pi).
\end{aligned}
}
\]

This equation is exact, not asymptotic.

---

## 3. Same-tail difference

Let

\[
Z:=H^V-H^W,
\qquad
R:=\Pi^V-\Pi^W
\]

for a same-tail pair.

M5-145 gives, for every finite `N`,

\[
\boxed{
Z(\xi,\eta,\theta)=O(\xi^{-N}),
\qquad
R(\xi,\eta,\theta)=O(\xi^{-N})
}
\]

on fixed compact genealogical/angular windows, with corresponding finite derivative versions.

Thus P1_B becomes a **superalgebraically decaying solution at `xi=+infinity`**.

---

## 4. Principal normal operator

Subtract the two exact inverse-Fuchsian equations.

The principal normal part is

\[
\boxed{
\mathcal N_\infty Z
:=4\nu Z_{\xi\xi}-Z_\xi.
}
\]

All purely linear genealogical/angular viscous terms carry coefficients

\[
O(\xi^{-1})\quad\text{or}\quad O(\xi^{-2}).
\]

The common-tail linearization of the nonlinear term contains `DZ`, with

\[
DZ=\partial_\eta Z+2\xi Z_\xi.
\]

Because the whole nonlinear term is multiplied by `xi^-2`, the normal derivative contribution is at worst

\[
O(\xi^{-1})Z_\xi.
\]

The remaining transport terms are `O(xi^-2)` times tangential/genealogical derivatives or `Z` itself.

Hence the critical `1/r` background is subprincipal in the inverse-Fuchsian normal direction.

---

## 5. Constant-coefficient normal spectrum

The homogeneous principal equation is

\[
4\nu f''-f'=0.
\]

Its characteristic exponents are

\[
\lambda=0,
\qquad
\lambda=\frac1{4\nu}.
\]

Therefore

\[
\boxed{
f(\xi)=C_0+C_1e^{\xi/(4\nu)}.}
\]

There is no decaying exponential branch at `+infinity`.

The boundary value `C_0` is already zero for a same-tail difference, while the second mode is forbidden by boundedness, let alone superalgebraic decay.

This is the inverse-coordinate form of M5-146/M5-147.

---

## 6. Pressure equation in inverse coordinates

The exact pressure operator becomes

\[
D^2-3D
=
\partial_\eta^2-3\partial_\eta
+4\xi\partial_{\eta\xi}
+4\xi^2\partial_{\xi\xi}
-2\xi\partial_\xi.
\]

Thus

\[
\boxed{
-\Bigl[
4\xi^2R_{\xi\xi}
+4\xi R_{\eta\xi}
-2\xi R_\xi
+(\partial_\eta^2-3\partial_\eta+2+\Delta_{S^2})R
\Bigr]
=\delta\mathcal Q.
}
\]

All algebraic homogeneous pressure multipoles have already been removed from the same-tail difference by M5-145.  Consequently any remaining pressure difference is itself superalgebraically decaying at infinity.

The unresolved issue is quantitative control of this flat pressure response relative to the flat velocity in a norm suitable for unique continuation.

---

## 7. Volterra/Carleman target

Write

\[
G:=Z_\xi.
\]

The principal equation has the first-order form

\[
4\nu G_\xi-G=\mathcal R,
\]

where `mathcal R` collects the `O(xi^-1)` coupled terms.

For a bounded decaying solution the formal terminal-at-infinity representation is

\[
\boxed{
G(\xi)
=-\frac1{4\nu}
 e^{\xi/(4\nu)}
\int_\xi^\infty
 e^{-s/(4\nu)}\mathcal R(s)\,ds.
}
\]

Hence a sufficient flat-uniqueness estimate would be a cross-section norm `X` in which

\[
\boxed{
\|\mathcal R(\xi)\|_X
\le
\frac{C}{\xi}
\bigl(
\|Z_\xi(\xi)\|_X
+\text{controlled lower-order flat norms}
\bigr)
}
\]

without an uncontrollable derivative loss from pressure.

For sufficiently large `xi`, the `C/xi` coefficient is perturbative relative to the one-way normal operator.

This is the concrete analytic gate behind P1_B.

---

## 8. DSD four-chain audit

### Formation — GREEN

`xi` is exactly `1/z`; no new asymptotic solution is introduced.

### Axis — GREEN

Normal infinity `xi`, genealogy `eta`, and sphere `theta` remain distinct channels.

### Static aggregation — GREEN

All algebraic pressure/velocity data are already removed before defining the flat remainder.

### Dynamics — GREEN

The forward-viscous sign produces a one-way normal spectrum `{0,+1/(4nu)}` rather than a decaying mode.

### Cross-audit — GREEN

M5-146 and M5-147 are recovered as the constant-coefficient normal limit of this exact equation.

---

## 9. Remaining technical obstruction

The flat velocity equation is perturbative in `1/xi`, but pressure is nonlocal in the original spatial variables and the genealogical direction is noncompact/aperiodic.

Therefore the missing theorem is not a new algebraic rigidity statement. It is a quantitative estimate proving that the coupled pressure/transport remainder is indeed perturbative in a suitable uniformly-local or invariant cross-section norm.

If such an estimate is established, the inverse-Fuchsian normal spectrum leaves no bounded superalgebraically decaying branch and P1_B closes.

Until then, this remains a YELLOW analytic gate.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]