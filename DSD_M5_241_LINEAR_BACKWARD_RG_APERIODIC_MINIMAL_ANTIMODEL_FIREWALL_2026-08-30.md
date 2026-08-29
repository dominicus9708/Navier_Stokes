# DSD M5-241 — Linear Backward-RG Aperiodic Minimal Anti-Model Firewall

Date: 2026-08-30

Parent: `DSD_M5_240_RG_FUCHSIAN_JET_IDENTIFICATION_AND_FLAT_COMPLETION_AUDIT_2026-08-30.md`

Status: **ANTI-PROOF FIREWALL / A COMPACT APERIODIC MINIMAL TRANSLATION HULL WITH A UNIFORM NONZERO RESIDUAL CAN LIE IN THE FINITE-TIME RANGE OF A BACKWARD-PARABOLIC EQUATION / THEREFORE MINIMAL APERIODICITY + RESIDUAL GAP + BACKWARD-RG REALIZABILITY IS NOT A CONTRADICTION AT THE FUNCTIONAL-ANALYTIC LEVEL / ANY CLOSURE MUST USE SPECIFIC 3D INCOMPRESSIBLE NAVIER--STOKES STRUCTURE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Purpose

M5-238--240 reduce the residual-active endpoint to

\[
\boxed{
\text{compact aperiodic minimal tail hull}
+
\mathbf F(T)\ge\varepsilon_{glob}>0
+
\text{one realized backward-RG completion}.
}
\]

It is tempting to regard backward parabolicity alone as incompatible with such recurrent boundary data.

This note gives an explicit linear countermodel to that inference.

---

## 2. Scalar linear RG model

Consider on the real log coordinate `y` the backward heat equation

\[
\boxed{
\partial_\rho u
=-\nu\partial_{yy}u,
\qquad
0\le\rho\le1.
}
\]

This has the same **anti-diffusive sign in the reconstruction variable** as the principal part of M5-237:

\[
\partial_\rho\mathscr R
=-\nu\Delta\mathscr R+\text{nonlinear terms}.
\]

---

## 3. Aperiodic minimal tail

Choose two rationally independent frequencies

\[
k_1=1,
\qquad
k_2=\sqrt2,
\]

and define

\[
\boxed{
f(y)=a\cos y+b\cos(\sqrt2\,y),
\qquad a,b\ne0.
}
\]

Its translation orbit is

\[
f_s(y)=f(y-s).
\]

The phase pair

\[
(s\bmod2\pi,
\sqrt2 s\bmod2\pi)
\]

is dense on the two-torus.

Hence the translation hull of `f` is compact, minimal, recurrent, and aperiodic.

There is no nonzero period `S` satisfying

\[
f(y-S)=f(y)
\]

for all `y`.

---

## 4. Uniform residual gap

For the linear stationary operator

\[
\mathcal F_{lin}(f)
:=
\nu f_{yy},
\]

we have

\[
\mathcal F_{lin}(f)
=-\nu a\cos y
-2\nu b\cos(\sqrt2 y).
\]

This is nonzero for every phase state in the hull.

In any translation-invariant cell metric controlling the two Fourier coefficients,

\[
\boxed{
\|\mathcal F_{lin}(f_s)\|
\ge c(a,b,\nu)>0
\quad\forall s.
}
\]

Thus the hull has a uniform residual gap from the linear stationary set.

---

## 5. Explicit backward-parabolic reconstruction

The solution with boundary value

\[
u(0,y)=f(y)
\]

is

\[
\boxed{
 u(\rho,y)
=
 a e^{\nu\rho}\cos y
+
 b e^{2\nu\rho}\cos(\sqrt2 y).
}
\]

Indeed

\[
\partial_\rho u
=
\nu a e^{\nu\rho}\cos y
+2\nu b e^{2\nu\rho}\cos(\sqrt2 y),
\]

while

\[
-\nu u_{yy}
=
\nu a e^{\nu\rho}\cos y
+2\nu b e^{2\nu\rho}\cos(\sqrt2 y).
\]

The solution exists smoothly for every finite

\[
0\le\rho\le1.
\]

So the aperiodic minimal tail lies in the finite-time range of the backward-parabolic reconstruction.

---

## 6. All-order jet is also harmless in the linear model

The Taylor coefficients are

\[
A_n(y)
=
\frac{\nu^n}{n!}
\left[
 a\cos y
+2^n b\cos(\sqrt2 y)
\right].
\]

The series converges for all finite `rho` because only finitely many frequencies are present.

Thus even the stronger package

\[
\boxed{
\text{aperiodic minimal hull}
+
\text{uniform residual gap}
+
\text{all-order determined convergent RG jet}
}
\]

is not contradictory in an anti-parabolic system.

---

## 7. What the anti-model does and does not show

It does **not** model:

- the three-dimensional divergence-free constraint;
- the `1/r` critical spatial geometry;
- pressure;
- quadratic Navier--Stokes mode coupling;
- point-force/stress constraints;
- the W1 first-hitting normalization.

It proves only the firewall

\[
\boxed{
\text{backward-parabolicity by itself}
\not\Rightarrow
\text{periodicity or stationarity of a compact minimal tail}.
}
\]

---

## 8. Consequence for strategy

A generic range theorem saying merely

\[
T\in\operatorname{Range}(\mathscr R_1)
\]

cannot be expected to eliminate the residual-active branch.

One needs a genuinely Navier--Stokes-specific obstruction involving at least one of:

1. divergence-free vector spherical harmonics;
2. pressure coupling;
3. quadratic generation of new log frequencies;
4. fixed stress/flux charges;
5. first-hitting core normalization and the positive core-speed floor.

Among these, item 3 is the next high-leverage target: an aperiodic finite-frequency tail under quadratic Navier--Stokes interaction generally generates sums and differences of log frequencies.  Audit whether closure of the compact minimal spectrum under this quadratic operation forces either an infinite frequency cascade/H channel or a finite resonant periodic module.

---

## 9. DSD verdict

### RED shortcut

\[
\text{aperiodic minimal}
+
\text{backward parabolic}
\Rightarrow
\text{impossible}
\]

is false in general.

### NEW TARGET

Use the **quadratic spectral closure** of stationary/Navier--Stokes residual and RG recursion rather than backward-parabolicity alone.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]