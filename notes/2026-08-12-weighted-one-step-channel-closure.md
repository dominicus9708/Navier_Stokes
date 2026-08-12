# One-step closure of the weighted moving-sphere channels

Date: 2026-08-12

Status: **DERIVED LOCAL ESTIMATES + OPEN FAR-HARMONIC / CASCADE OBLIGATION**.

This note continues the primary proof track after the moving weighted-variance lemma.  The purpose is to determine which of the three signed redistribution channels are genuinely independent at one scale.

## 1. Setup

Fix a scale `ell>0` and let the smooth moving cutoff be

\[
\varphi_\ell(x,t)=\phi_\ell(x-X_\ell(t)),
\qquad
\dot X_\ell=\bar U_\ell,
\]

where `bar U_ell` is the cutoff-weighted mean velocity and

\[
v=u-\bar U_\ell,
\qquad
\int \varphi_\ell v\,dx=0.
\]

Use a fixed parent factor

\[
R=4\ell
\]

and define, at the same center `X_ell(t)`,

\[
C_R(t)
=R^{-1}\int_{B_R(X_\ell(t))}
|u-(u)_{B_R}|^2dx,
\]

\[
E_R(t)
=R\int_{B_R(X_\ell(t))}|\nabla u|^2dx.
\]

Both are invariant under the Navier--Stokes scaling.

The moving weighted-variance lemma gives schematically

\[
\frac12\frac{d}{d\tau}C_\phi
+D_\phi
\le
A_\phi+P_\phi+B_\phi,
\qquad
\tau=\frac{t-t_0}{\ell^2},
\]

where

\[
D_\phi=\nu\ell\int\varphi_\ell|\nabla u|^2dx,
\]

and the right side contains relative advection, pressure work, and the cutoff-Laplacian viscous term.

All estimates below use only fixed-shape cutoff constants.

## 2. Parent-scale control of the moving-frame velocity

Although `v` is centered with the weighted inner mean rather than the ordinary mean on `B_R`, the two constants differ by an amount controlled by the parent oscillation.

Let

\[
c_R=(u)_{B_R}.
\]

Since the cutoff mass is comparable to `ell^3`, Cauchy--Schwarz gives

\[
|\bar U_\ell-c_R|
\lesssim
\ell^{-3/2}
\|u-c_R\|_{L^2(B_R)}.
\]

Consequently, on the support of the inner cutoff and its derivatives,

\[
\|v\|_2
\lesssim
\|u-c_R\|_{L^2(B_R)}.
\]

Poincare--Sobolev on `B_R` also gives

\[
\|v\|_6
\lesssim
\|\nabla u\|_{L^2(B_R)}.
\]

Interpolating between `L^2` and `L^6`,

\[
\boxed{
\int_{B_{2\ell}(X_\ell)}|v|^3dx
\lesssim
(C_RE_R)^{3/4}.
}
\]

Equivalently,

\[
\|v\|_{L^3(B_{2\ell})}
\lesssim
(C_RE_R)^{1/4}.
\]

This is the basic one-step critical interpolation channel.

## 3. Relative-advection channel

Because

\[
|\nabla\phi_\ell|\lesssim \ell^{-1},
\]

the scale-normalized advective contribution satisfies

\[
A_\phi
:=
\ell\left|
\int\frac{|v|^2}{2}
v\cdot\nabla\varphi_\ell dx
\right|
\lesssim
\int_{B_{2\ell}}|v|^3dx.
\]

Therefore

\[
\boxed{
A_\phi
\lesssim
(C_RE_R)^{3/4}.
}
\]

Thus relative advection is not an independent one-scale quantity once parent oscillation and dissipation are retained.

## 4. Cutoff-viscous channel

Similarly,

\[
|\Delta\phi_\ell|
\lesssim
\ell^{-2}.
\]

Hence

\[
B_\phi
:=
\frac{\nu\ell}{2}
\left|
\int|v|^2\Delta\varphi_\ell dx
\right|
\lesssim
\nu\ell^{-1}
\int_{B_{2\ell}}|v|^2dx.
\]

The parent-scale comparison yields

\[
\boxed{
B_\phi
\lesssim
\nu C_R.
}
\]

This is a lower-order scale-critical localization cost.  It is not a new nonlinear amplification channel.

## 5. Split pressure into near and far parts

Choose a smooth cutoff `chi` supported in `B_R(X_ell)` and equal to one on `B_{2 ell}(X_ell)`.

Because `bar U_ell` is spatially constant and `div u=0`,

\[
\partial_i\partial_j(v_i v_j)
=
\partial_i\partial_j(u_i u_j).
\]

Define the localized near pressure by the whole-space Riesz transforms

\[
p_{\rm near}
=\mathcal R_i\mathcal R_j
\bigl(\chi v_i v_j\bigr).
\]

Then

\[
p_{\rm far}=p-p_{\rm near}
\]

is harmonic on the inner region where `chi=1`.

Calderon--Zygmund boundedness gives

\[
\|p_{\rm near}\|_{3/2}
\lesssim
\|v\|_3^2.
\]

Therefore the normalized near-pressure work satisfies

\[
\begin{aligned}
P_{\rm near}
&:=
\ell\left|
\int p_{\rm near}
v\cdot\nabla\varphi_\ell dx
\right|\\
&\lesssim
\|p_{\rm near}\|_{3/2}
\|v\|_3,
\end{aligned}
\]

so

\[
\boxed{
P_{\rm near}
\lesssim
(C_RE_R)^{3/4}.
}
\]

**Consequence:** at one scale, the near pressure belongs to the same critical nonlinear block as relative advection.  It should not be kept as an independent scalar danger channel.

## 6. Affine-free far harmonic pressure

The far part is harmonic in the inner ball.  More importantly, the pressure work is insensitive to affine pressure components.

For any time-dependent scalar `a(t)`,

\[
\int a\,v\cdot\nabla\varphi_\ell dx=0
\]

because `div v=0`.

For any time-dependent vector `b(t)`, integration by parts gives

\[
\int
[b\cdot(x-X_\ell)]
v\cdot\nabla\varphi_\ell dx
=-b\cdot\int\varphi_\ell vdx
=0.
\]

Thus define the affine-free harmonic-tail channel

\[
\boxed{
H_\ell(t)
=
\inf_{a\in\mathbb R,\ b\in\mathbb R^3}
\|p_{\rm far}-a-b\cdot(x-X_\ell)\|_{L^{3/2}(B_{2\ell})}.
}
\]

`H_ell` is Navier--Stokes scale invariant.

The far-pressure contribution obeys

\[
\boxed{
P_{\rm far}
\lesssim
H_\ell(C_RE_R)^{1/4}.
}
\]

This is now the only pressure quantity left by the one-step closure.

The previous pressure-difference localization note explains why kernel differences/Taylor subtraction improve the decay of genuinely remote sources.  A fully velocity-only estimate of `H_ell` compatible with the present moving weighted cutoff remains to be written carefully; it is not assumed here.

## 7. One-step scale-transfer inequality

Combining the preceding estimates gives the structural inequality

\[
\boxed{
\frac12\frac{d}{d\tau}C_\phi
+D_\phi
\lesssim
(C_RE_R)^{3/4}
+
H_\ell(C_RE_R)^{1/4}
+
\nu C_R.
}
\]

Here `R=4 ell` and `tau=(t-t0)/ell^2`.

This is a **parent-to-child scale transfer inequality**.  It is not a closed a-priori estimate because the child scale is fed by parent-scale oscillation/dissipation and by the affine-free far harmonic tail.

## 8. Time-integrated form

On a parabolic interval of normalized length at most one, Holder gives schematically

\[
\int(C_RE_R)^{3/4}d\tau
\le
(\sup C_R)^{3/4}
\left(\int E_Rd\tau\right)^{3/4},
\]

and

\[
\int H_\ell(C_RE_R)^{1/4}d\tau
\le
(\sup H_\ell)
(\sup C_R)^{1/4}
\left(\int E_Rd\tau\right)^{1/4}.
\]

Thus the same oscillation--dissipation products that feed the known pressure-free epsilon-regularity bridge also govern the nonlinear input into the child sphere.

## 9. What this does and does not achieve

### Closed at one step

- coherent translation: removed by the weighted moving center;
- relative advection: controlled by parent `C_R,E_R`;
- cutoff viscous localization: controlled linearly by `C_R`;
- near pressure: controlled by the same cubic block as advection;
- constant and linear far pressure: exactly irrelevant to the variance budget.

### Still open

1. obtain a velocity-only, non-circular control of the affine-free harmonic tail `H_ell` in the exact moving-cutoff setting;
2. show that the parent-to-child recursion cannot sustain a critical cascade at arbitrarily small scales;
3. or show that sustaining such a cascade forces an already known regularity gate (vorticity-direction coherence, middle-strain control, etc.).

The global finite-energy bound alone cannot rule out a nested critical cascade: a scale-critical profile may carry only `O(ell)` kinetic energy inside `B_ell` at each shrinking scale.

## 10. DSD interpretation

The four-paper DSD split now becomes sharper.

- **Formation:** distinguish the inner oscillation, parent oscillation, dissipation, and harmonic-tail channels.
- **Axis-property layer:** retain directional strain/vorticity information for any later obstruction to persistent cascade.
- **Static Aggregation:** treat scales as indexed channels rather than collapse all radii to one global scalar.
- **Structural Reorganization Dynamics:** the one-step inequality is a directed parent-to-child transfer rule.

The next DSD object should therefore be a **multiscale cascade block**, not another single-scale scalar.

Status: **OPEN CASCADE OBLIGATION**.
