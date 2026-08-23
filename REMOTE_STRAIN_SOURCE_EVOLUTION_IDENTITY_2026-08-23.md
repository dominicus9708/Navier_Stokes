# Remote Strain Source Evolution Identity — 2026-08-23

Status: **EXACT S-LEVEL EVOLUTION IDENTITY ON THE ORIGINAL SMOOTH SOLUTION — GLOBAL REGULARITY NOT PROVED.**

This note attacks the remaining source-replacement ambiguity inside dynamically active `H_remote`. Instead of attempting to identify one material packet across stages, track the actual remote Biot--Savart strain functional with a smooth, possibly time-dependent radial cutoff.

The resulting identity is exact. It shows that remote normalized strain can change or be maintained only through bulk source transport, cutoff-relative shell crossing, vorticity stretching, or a viscous annular commutator. Pressure does not appear because the calculation is performed in vorticity form.

## 1. Normalized vorticity equation

Use the fixed-center first-hitting normalization

\[
y=M(t)^{1/2}(x-X_*),
\qquad
\frac{ds}{dt}=M(t),
\]

\[
U=M^{-1/2}u,
\qquad
\Omega=M^{-1}\omega,
\qquad
\Sigma=M^{-1}S,
\]

and

\[
b=(\log M)_s\ge0.
\]

Since

\[
(\omega\cdot\nabla)u=S\omega
\]

(the antisymmetric part annihilates `omega`), the physical vorticity equation gives exactly

\[
\boxed{
\Omega_s
+U\cdot\nabla\Omega
+\frac b2y\cdot\nabla\Omega
+b\Omega
=\Sigma\Omega+\nu\Delta\Omega.
}
\]

This is an identity on every finite smooth first-hitting stage.

## 2. Remote strain kernel

For a smooth rapidly decaying divergence-free field in `R^3`, normalized strain at the origin is a singular integral of normalized vorticity,

\[
\Sigma(0,s)=\operatorname{p.v.}\int K(y)\Omega(y,s)dy,
\]

where the matrix-valued kernel `K` is homogeneous of degree `-3`:

\[
K(\lambda y)=\lambda^{-3}K(y).
\]

Its components are second derivatives of the Newtonian potential (up to fixed rotations/symmetrization), hence

\[
\boxed{\Delta K=0\qquad(y\ne0).}
\]

Only homogeneity and smoothness away from the origin are used below.

## 3. Smooth remote cutoff

Choose a fixed radial profile `psi` such that

\[
\psi(\rho)=0\quad(\rho\le1),
\qquad
\psi(\rho)=1\quad(\rho\ge2),
\]

and define for a positive piecewise-`C1` radius `R(s)`

\[
\psi_R(y,s)=\psi(|y|/R(s)).
\]

Then

\[
\boxed{
\partial_s\psi_R
=-\frac{R_s}{R}\,y\cdot\nabla\psi_R.
}
\]

Define the smooth remote strain functional

\[
\boxed{
\mathcal S_R(s)
:=\int K(y)\psi_R(y,s)\Omega(y,s)dy.
}
\]

It is the strain contribution of the exterior, with a smooth transition on the annulus

\[
A_R=\{R<|y|<2R\}.
\]

## 4. Exact differentiation

Differentiate `S_R` and insert the normalized vorticity equation. For the advective term use `div U=0`:

\[
-\int K\psi_R(U\cdot\nabla\Omega)
=
\int U\cdot\nabla(K\psi_R)\,\Omega.
\]

For the dilation term,

\[
-\frac b2\int K\psi_R(y\cdot\nabla\Omega)
=
\frac b2\int \nabla\cdot(yK\psi_R)\Omega.
\]

Because `K` has degree `-3`,

\[
3K+y\cdot\nabla K=0,
\]

and therefore

\[
\nabla\cdot(yK\psi_R)
=K(y\cdot\nabla\psi_R).
\]

For viscosity, rapid decay allows two integrations by parts:

\[
\int K\psi_R\Delta\Omega
=
\int\Delta(K\psi_R)\Omega.
\]

Combining all terms gives

\[
\boxed{
\begin{aligned}
(\partial_s+b)\mathcal S_R
&=
\underbrace{\int\psi_R(U\cdot\nabla K)\Omega}_{\mathcal T_{bulk}}\\
&\quad+
\underbrace{\int K
\left[
U+\left(\frac b2-\frac{R_s}{R}\right)y
\right]\cdot\nabla\psi_R\,\Omega}_{\mathcal T_{cut}}\\
&\quad+
\underbrace{\int K\psi_R(\Sigma\Omega)}_{\mathcal X_{stretch}}\\
&\quad+
\underbrace{\nu\int\Delta(K\psi_R)\Omega}_{\mathcal V_{ann}}.
\end{aligned}
}
\]

This is the desired exact source-evolution identity.

## 5. Physical-radius form of the cutoff term

The physical cutoff radius is

\[
\boxed{
\ell(s)=\frac{R(s)}{M(s)^{1/2}}.
}
\]

Since

\[
(\log\ell)_s
=\frac{R_s}{R}-\frac b2,
\]

we have

\[
\frac b2-\frac{R_s}{R}
=-\frac{\ell_s}{\ell}.
\]

Hence

\[
\boxed{
\mathcal T_{cut}
=
\int K
\left[
U-\frac{\ell_s}{\ell}y
\right]\cdot\nabla\psi_R\,\Omega.
}
\]

This has a direct interpretation:

- `U·grad psi_R` measures material source crossing of the cutoff;
- `-(ell_s/ell)y·grad psi_R` measures change of the physical diagnostic/source radius itself.

Thus effective source replacement by inward movement of the active physical radius is represented explicitly rather than hidden in a relabeling argument.

Special cases:

- fixed normalized radius `R`: `ell_s/ell=-b/2`, recovering the normalization/dilation sweep;
- fixed physical radius `ell`: `R_s/R=b/2`, so the artificial dilation sweep vanishes and only actual material crossing remains.

## 6. Viscosity is purely annular

Because `psi_R=0` near the origin, `psi_R=1` outside `2R`, and `Delta K=0` away from zero,

\[
\boxed{
\Delta(K\psi_R)
=
2\nabla K\cdot\nabla\psi_R
+K\Delta\psi_R,
}
\]

which is supported entirely in `A_R`.

Using

\[
|K|\lesssim R^{-3},
\qquad
|\nabla K|\lesssim R^{-4},
\qquad
|\nabla\psi_R|\lesssim R^{-1},
\qquad
|\Delta\psi_R|\lesssim R^{-2},
\]

we get

\[
\boxed{
\|\Delta(K\psi_R)\|_2
\lesssim R^{-7/2}.
}
\]

Therefore

\[
\boxed{
|\mathcal V_{ann}|
\lesssim
\nu R^{-7/2}
\|\Omega\|_{L^2(A_R)}.
}
\]

A fixed positive viscous source-evolution action at `R->infinity` consequently requires an extremely large annular enstrophy occupancy; this is quantified below.

## 7. Bulk transport is small under the existing Morrey corridor

Assume the same scale-invariant local kinetic-energy control used in the parent-pressure gate:

\[
\rho^{-1}\int_{B_\rho}|U|^2dy\le M_*
\]

for the remote parent radii under consideration, and use the first-hitting cap

\[
\|\Omega\|_\infty\le1.
\]

On a dyadic annulus of radius `rho`,

\[
\|U\|_2\lesssim M_*^{1/2}\rho^{1/2},
\qquad
\|\Omega\|_2\lesssim \rho^{3/2}.
\]

Since `|grad K|\lesssim rho^(-4)`, the annular contribution satisfies

\[
\int_{A_\rho}|U||\Omega||\nabla K|
\lesssim
M_*^{1/2}\rho^{-2}.
\]

Summing dyadically gives

\[
\boxed{
|\mathcal T_{bulk}|
\lesssim
M_*^{1/2}R^{-2}.
}
\]

The material part of the cutoff term satisfies the same scale:

\[
\boxed{
\left|
\int K(U\cdot\nabla\psi_R)\Omega
\right|
\lesssim
M_*^{1/2}R^{-2}.
}
\]

Thus, within the existing Morrey/no-local-energy-turnover corridor, ordinary remote advection cannot pay an order-one source-maintenance action as `R->infinity`.

Failure of the Morrey corridor is already a typed local-energy/turnover exit.

## 8. Radius-sweep term is scale critical

By the first-hitting cap `|Omega|<=1`,

\[
\begin{aligned}
\left|
\int K
\left(-\frac{\ell_s}{\ell}y\right)
\cdot\nabla\psi_R\,\Omega
\right|
&\lesssim
\left|\frac{\ell_s}{\ell}\right|
R^{-3}R R^{-1}|A_R|\\
&\lesssim
\left|\frac{\ell_s}{\ell}\right|.
\end{aligned}
\]

Therefore

\[
\boxed{
|\mathcal T_{sweep}|
\lesssim
|\partial_s\log\ell|.
}
\]

This is exactly scale invariant. The logarithmic physical-radius action previously found in the active-H packing calculation is therefore the natural turnover/source-replacement action appearing in the exact evolution identity.

## 9. Fixed viscous action gives an R^7 occupancy tax

Suppose on a stage with `R(s)>=R_-` the viscous contribution pays action

\[
\int_I|\mathcal V_{ann}|ds\ge v_0>0.
\]

Then by Cauchy--Schwarz in time,

\[
v_0^2
\lesssim
\nu^2 R_-^{-7}
L_j
\int_I\|\Omega\|_{L^2(A_{R(s)})}^2ds.
\]

Hence

\[
\boxed{
\int_I\|\Omega\|_{L^2(A_{R(s)})}^2ds
\gtrsim
\nu^{-2}R_-^7\frac{v_0^2}{L_j}.
}
\]

On an infinite geometric first-hitting sequence with `R_->infinity`, repeated fixed viscous action is therefore even more expensive than the direct `R^3` active-strain tax and is incompatible with the finite physical kinetic-energy dissipation packing unless the radius ceases to be remote.

## 10. Integrated stage identity

Let

\[
B(s)=\int_{s_0}^s b(\sigma)d\sigma.
\]

Then

\[
\boxed{
\partial_s\left(e^{B(s)}\mathcal S_R(s)\right)
=e^{B(s)}
\left(
\mathcal T_{bulk}
+\mathcal T_{cut}
+\mathcal X_{stretch}
+\mathcal V_{ann}
\right).
}
\]

Over one full geometric stage,

\[
B(s_1)=\log q,
\]

so

\[
\boxed{
q\mathcal S_{R_1}(s_1)
-\mathcal S_{R_0}(s_0)
=
\int_{I_j}e^{B(s)}
\left(
\mathcal T_{bulk}
+\mathcal T_{cut}
+\mathcal X_{stretch}
+\mathcal V_{ann}
\right)ds.
}
\]

Here `R_0=R(s_0)` and `R_1=R(s_1)`.

This formula remains valid even when the remote payer at the final time is not the same material packet as the payer at the initial time.

## 11. Persistence tax independent of source identity

Let

\[
F_j
:=
\int_{I_j}e^{B(s)-B(s_j)}
\left(
|\mathcal T_{bulk}|
+|\mathcal T_{cut}|
+|\mathcal X_{stretch}|
+|\mathcal V_{ann}|
\right)ds.
\]

The stage identity implies

\[
\boxed{
q|\mathcal S_{j+1}|
\le
|\mathcal S_j|+F_j.
}
\]

Suppose an adaptive remote-source path satisfies at the geometric checkpoints

\[
a_0\le|\mathcal S_j|\le B_0
\]

for all stages in a consecutive active block. Summing gives

\[
\sum_{j=J_0}^{J-1}F_j
\ge
(q-1)\sum_{j=J_0+1}^{J-1}|\mathcal S_j|
+q|\mathcal S_J|-|\mathcal S_{J_0}|.
\]

Therefore

\[
\boxed{
\sum_{j=J_0}^{J-1}F_j
\ge
(q-1)a_0(J-J_0-1)-B_0.
}
\]

In particular, an arbitrarily long active remote-strain corridor must pay a fixed positive average source-evolution action, irrespective of whether the source is materially persistent or repeatedly replaced.

This removes the need for a same-packet matching hypothesis at the branch-routing level.

## 12. Branch routing

At large remote radius and within the existing Morrey corridor:

- `T_bulk` and the material part of `T_cut` are `O(R^-2)` and cannot supply fixed late-stage action;
- a large radius-sweep part of `T_cut` is exactly the logarithmic physical shell/source replacement action `T_R`;
- a fixed `V_ann` action pays an `R^7` enstrophy-time tax and is globally unsustainable at `R->infinity`;
- the only remaining order-one source-maintenance term is
  \[
  \boxed{\mathcal X_{stretch}=\int K\psi_R(\Sigma\Omega),}
  \]
  i.e. actual remote vorticity stretching/reorientation.

Thus, modulo the already typed Morrey failure and finite cutoff regularity assumptions,

\[
\boxed{
H_{remote}^{active}
\Longrightarrow
T_R
\ \lor\ 
\text{remote stretching/projective action}
\ \lor\ 
\text{global energy contradiction}.
}
\]

The last genuine source-replacement mechanism has therefore been reduced to an explicit vorticity-stretching term rather than an unidentified payer switch.

## 13. Current next target

The remaining question is now precise:

> Can the remote stretching term
> \[
> \mathcal X_{stretch}
> =\int K\psi_R(\Sigma\Omega)
> \]
> supply a fixed positive source-maintenance action on infinitely many remote stages without either (i) requiring an active far strain already covered by the `R^3` enstrophy tax, (ii) using local/parent strain that transports projective action into the remote shell, or (iii) creating shell turnover?

This is now a bilinear strain-vorticity source problem rather than a vague source-replacement problem.

Status: **THE REMOTE-STRAIN PAYER HAS AN EXACT EVOLUTION LAW. SOURCE REPLACEMENT NO LONGER REQUIRES MATERIAL PACKET MATCHING: LONG-LIVED ACTIVE REMOTE STRAIN MUST PAY A FIXED AVERAGE ACTION THROUGH PHYSICAL-RADIUS SWEEP, REMOTE VORTICITY STRETCHING, OR A GLOBALLY UNSUSTAINABLE VISCOUS/ENERGY COST. GLOBAL REGULARITY IS NOT PROVED.**
