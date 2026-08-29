# DSD M5-258 — Stationary Log-Tail Head-Pressure Identity

Date: 2026-08-30

Parent: `DSD_M5_257_RENORMALIZED_RG_RESIDUAL_SQUARE_AND_LYAPUNOV_FIREWALL_2026-08-30.md`

Status: **EXACT STATIONARY-SUBBRANCH IDENTITY / THE HEAD PRESSURE `H=P+|T|^2/2` OF A STATIONARY CRITICAL TAIL SATISFIES THE SCALAR ELLIPTIC-ADVECTION EQUATION `-nu Delta H+T·grad H=-nu|omega|^2`; IN LOG-RADIUS VARIABLES `T=r^-1 Phi`, `H=r^-2 h`, THE INVARIANT LOG-AVERAGE GIVES `2nu<h>+<Phi_r h>=nu<|Omega|^2>` / THIS LINKS RADIAL BERNOULLI CORRELATION DIRECTLY TO VORTICITY ENSTROPHY AND MEAN HEAD PRESSURE / WHOLE-SPACE MAXIMUM-PRINCIPLE SIGN RESULTS DO NOT TRANSFER AUTOMATICALLY ACROSS THE POINT-FORCE PUNCTURE / GLOBAL REGULARITY UNPROVED.**

---

## 1. Stationary critical tail

Return to the stationary branch of M5-220/M5-227.

Let

\[
T(x)=\frac1r\Phi(y,\theta),
\qquad
P(x)=\frac1{r^2}\Pi(y,\theta),
\qquad
y=\log r.
\]

The stationary equation on `R3\{0}` is

\[
-\nu\Delta T+(T\cdot\nabla)T+\nabla P=0,
\qquad
\nabla\cdot T=0.
\]

Let

\[
\omega=\nabla\times T
=\frac1{r^2}\Omega(y,\theta).
\]

Define the head pressure

\[
\boxed{
H:=P+\frac12|T|^2
=\frac1{r^2}h(y,\theta),
}
\]

where

\[
\boxed{
h:=\Pi+\frac12|\Phi|^2.}
\]

---

## 2. Exact head-pressure equation

For every smooth stationary incompressible Navier--Stokes solution,

\[
\boxed{
-\nu\Delta H+T\cdot\nabla H
=-\nu|\omega|^2.
}
\]

Equivalently,

\[
\boxed{
\Delta H-\frac1\nu T\cdot\nabla H
=|\omega|^2\ge0.
}
\]

This is the standard stationary Bernoulli/head-pressure identity.

A direct derivation is obtained by dotting the momentum equation with `T`, taking divergence of the momentum equation, and using

\[
|\nabla T|^2-\partial_iT_j\partial_jT_i
=|\omega|^2.
\]

---

## 3. Log-cylinder formulae

For a scalar degree-`-2` field

\[
f=r^{-2}h(y,\theta),
\qquad y=\log r,
\]

one has

\[
\boxed{
\Delta f
=
\frac1{r^4}
\left(
 h_{yy}-3h_y+2h+\Delta_{S^2}h
\right).
}
\]

Also

\[
\nabla H
=
\frac1{r^3}
\left[
(h_y-2h)e_r+\nabla_{S^2}h
\right].
\]

Therefore

\[
T\cdot\nabla H
=
\frac1{r^4}
\left[
\Phi_r(h_y-2h)
+\Phi_\tau\cdot\nabla_{S^2}h
\right].
\]

The head-pressure equation becomes

\[
\boxed{
\nu
\left(
 h_{yy}-3h_y+2h+\Delta_{S^2}h
\right)
-
\Phi_r(h_y-2h)
-
\Phi_\tau\cdot\nabla_{S^2}h
=
\nu|\Omega|^2.
}
\]

---

## 4. Divergence-free cylinder identity

For

\[
T=r^{-1}(\Phi_re_r+\Phi_\tau),
\]

incompressibility gives

\[
\boxed{
\partial_y\Phi_r
+\Phi_r
+\operatorname{div}_{S^2}\Phi_\tau
=0.
}
\]

This identity is essential in the averaged head-pressure calculation.

---

## 5. Sphere and invariant-log average

Integrate the cylinder head-pressure equation over `S2`, then take any invariant mean in `y` on the compact recurrent log-translation hull.

All exact `y` derivatives and spherical divergences average to zero.

The advection terms combine as follows:

\[
\begin{aligned}
&-\Phi_r h_y
+2\Phi_r h
-\Phi_\tau\cdot\nabla_Sh\\
&\quad\rightsquigarrow
-\Phi_rh_y
+2\Phi_rh
+h\operatorname{div}_S\Phi_\tau\\
&\quad=
-\Phi_rh_y
+\Phi_rh
-h\partial_y\Phi_r.
\end{aligned}
\]

The first and third terms form

\[
-\partial_y(\Phi_rh),
\]

whose invariant mean vanishes.

Hence the exact recurrent identity is

\[
\boxed{
2\nu
\left\langle
\int_{S^2}h\,d\theta
\right\rangle
+
\left\langle
\int_{S^2}\Phi_rh\,d\theta
\right\rangle
=
\nu
\left\langle
\int_{S^2}|\Omega|^2d\theta
\right\rangle.
}
\]

---

## 6. Bernoulli radial-flux form

Define

\[
\overline H_0
:=
\left\langle\int_{S^2}h\right\rangle,
\]

\[
\mathcal B_r
:=
\left\langle\int_{S^2}h\Phi_r\right\rangle,
\]

and

\[
\mathcal Z_T
:=
\left\langle\int_{S^2}|\Omega|^2\right\rangle.
\]

Then

\[
\boxed{
\mathcal B_r
=
\nu\mathcal Z_T
-2\nu\overline H_0.
}
\]

Thus radial Bernoulli correlation is not an independent stationary-tail scalar: it is fixed by enstrophy and the invariant mean head pressure.

---

## 7. Useful sign subbranches

If one can prove

\[
\overline H_0\le0,
\]

then immediately

\[
\boxed{
\mathcal B_r
\ge
\nu\mathcal Z_T>0
}
\]

for every nonzero stationary tail.

More generally, if

\[
\overline H_0
\le
\left(\frac12-\delta\right)\mathcal Z_T
\]

in viscosity-normalized units, then

\[
\boxed{
\mathcal B_r
\ge
2\delta\nu\mathcal Z_T.
}
\]

Thus control of the mean head pressure would immediately create a strict radial Bernoulli payer.

---

## 8. Maximum-principle scope firewall

For smooth stationary solutions on the **whole space** with finite Dirichlet integral and head pressure tending to zero at infinity, the scalar equation and maximum principle imply a nonpositive head pressure under the standard hypotheses used in stationary Liouville theory.

The present stationary endpoint is different:

\[
-\nu\Delta T+(T\cdot\nabla)T+\nabla P
=b\delta_0
\]

in the whole-space distributional sense and is only smooth on `R3\{0}`.

The origin is therefore an inner singular boundary for the classical maximum-principle argument.

Consequently

\[
\boxed{
H\le0
\text{ on the current point-force branch}
}

is **not** imported automatically from smooth whole-space Liouville theorems.

A separate punctured/point-force sign theorem would be required.

---

## 9. Relation to M5-245 and M5-231

M5-245 identified radial Bernoulli correlation as the necessary payment in the energy-transverse residual branch.

The present stationary identity shows that on an actual stationary critical profile this correlation is exactly

\[
\nu\mathcal Z_T-2\nu\overline H_0.
\]

Thus the previously separate pressure-radial and kinetic-radial terms can be recombined into one head-pressure observable on the stationary branch.

This does not close the branch because the sign and size of `Hbar_0` remain uncontrolled at arbitrary point-force amplitude.

---

## 10. Additional head-pressure energy identity

Multiply the cylinder head-pressure equation by `h` and take the invariant sphere/log mean.

Integration by parts gives

\[
\boxed{
\nu
\left\langle
\int_{S^2}
\bigl(|h_y|^2+|\nabla_Sh|^2\bigr)
\right\rangle
=
2\nu\langle\!\int h^2\rangle
+
\frac32\langle\!\int\Phi_rh^2\rangle
-
\nu\langle\!\int|\Omega|^2h\rangle.
}
\]

This is exact but not sign-definite at arbitrary amplitude.

It records the next available route if a sign/size control on `h` or `Phi_r` is obtained.

---

## 11. DSD verdict

### PROVED

\[
\boxed{
2\nu\overline H_0+\mathcal B_r
=\nu\mathcal Z_T.
}
\]

### POTENTIALLY STRONG

Any theorem forcing

\[
\overline H_0\le0
\]

would give a strict positive radial Bernoulli-flux floor.

### FIREWALL

Smooth-whole-space maximum-principle sign results are not automatically valid across the point-force puncture.

### NEXT TARGET

Audit the head pressure of the explicit Landau family and of the fixed-force stationary linearized/dilation mode. Determine whether the point-force structure itself enforces a sign or an averaged upper bound on `h` that survives beyond the Landau branch.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
