# DSD M17-384 — Exact CE-H material multiplier transport preserves vanishing order and routes finite-scale doubling growth to flow or strain inhomogeneity

Date: 2026-09-08  
Canonical ID: **M17-384**

Status: **ACTIVE MATERIAL-DOUBLING TRANSPORT THEOREM / M17-383 DYNAMICAL REFINEMENT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M17-383

M17-383 introduced the local mass-doubling deficit

\[
\mathfrak D_\theta(x,R,t)
:=
\log\frac{E_t(B_R(x))}{E_t(B_{\theta R}(x))},
\qquad
E_t(A):=\int_A|\Omega(x,t)|^2dx,
\]

and showed that bounded `D_theta` gives the inner/outer mass retention needed for the late M17 scale-comparable packet construction.

It also proved that coefficient regularity alone cannot bound `D_theta`: even constant-coefficient divergence-free Helmholtz fields can have arbitrarily large local vanishing order.

The remaining question is therefore dynamical:

> can exact CE-H Navier--Stokes dynamics create or strongly amplify local doubling/frequency without paying through another already typed channel?

The present module separates asymptotic vanishing order from finite-scale doubling and gives the exact material transport law for both.

## 2. Physical exact CE-H equations

Work in physical variables on a smooth regular CE-H interval.

Let

\[
\Omega=\nabla\times u,
\qquad
\rho=|\Omega|,
\qquad
\xi=\Omega/\rho
\]

on the active set.

Exact CE-H gives

\[
\boxed{\Delta\Omega=\kappa\Omega}
\]

and the strain eigenvector relation

\[
\boxed{\Sigma\xi=\sigma\xi.}
\]

For incompressible Navier--Stokes with viscosity `nu`, the vorticity equation is

\[
D_t\Omega
=
(\Omega\cdot\nabla)u
+
\nu\Delta\Omega.
\]

Because the antisymmetric part of `nabla u` annihilates the vorticity direction,

\[
(\Omega\cdot\nabla)u
=
\Sigma\Omega
=
\sigma\Omega.
\]

Therefore on exact CE-H,

\[
\boxed{
D_t\Omega
=
\lambda\Omega,
\qquad
\lambda:=\sigma+\nu\kappa.
}
\]

This is an exact scalar-multiplier material law.

## 3. Exact Lagrangian representation

Let `X(a,t)` be the incompressible material flow,

\[
\partial_tX(a,t)=u(X(a,t),t),
\qquad
X(a,t_0)=a.
\]

Define

\[
\Lambda(a;t_0,t)
:=
\int_{t_0}^{t}
\lambda(X(a,s),s)\,ds.
\]

Then the scalar ODE from Section 2 gives

\[
\boxed{
\Omega(X(a,t),t)
=
 e^{\Lambda(a;t_0,t)}\Omega(a,t_0).
}
\]

The multiplier is strictly positive and finite as long as the regular CE-H branch remains smooth.

Because the velocity is incompressible,

\[
\boxed{\det D_aX(a,t)=1.}
\]

Hence no Jacobian density is introduced when transporting `L2` mass through material sets.

## 4. Material nodal set is transported exactly

The representation immediately gives

\[
\Omega(a,t_0)=0
\iff
\Omega(X(a,t),t)=0.
\]

Thus, while the smooth exact CE-H branch persists,

\[
\boxed{
\mathcal Z_t
=X(t,t_0)\mathcal Z_{t_0},
}
\]

where

\[
\mathcal Z_t:=\{x:\Omega(x,t)=0\}.
\]

No new vorticity zero can be born inside the regular same-material CE-H branch, and no existing zero can disappear there.

Any true nodal creation/destruction must therefore pass through at least one of

\[
G_{CEH/rank\ loss},
\quad
G_{flow/domain\ loss},
\quad
G_{interface/genealogy\ change},
\]

or another failure of the hypotheses used above.

## 5. Pointwise vanishing order is materially invariant

Fix a material label `a_0` and its trajectory

\[
x_t=X(a_0,t).
\]

Assume the flow map is a local `C^1` diffeomorphism and `Lambda` is smooth near `a_0`.

Near `a_0`,

\[
\Omega_0(a)
:=
\Omega(a,t_0)
\]

is transformed into

\[
\Omega_t(x)
=
 m_t(a)\Omega_0(a),
\qquad
x=X(a,t),
\]

with

\[
m_t(a)=e^{\Lambda(a;t_0,t)}>0.
\]

Multiplication by a smooth nonvanishing scalar does not change the first nonzero jet order, and composition with a local diffeomorphism with nonsingular derivative also preserves that order.

Therefore

\[
\boxed{
\operatorname{ord}_{x_t}\Omega(\cdot,t)
=
\operatorname{ord}_{a_0}\Omega(\cdot,t_0).
}
\]

This is stronger than a bound on an instantaneous doubling index: the asymptotic vanishing order itself is an exact material invariant on the smooth CE-H branch.

Consequently an unbounded sequence of vanishing orders along descendant CE-H packets cannot be dynamically manufactured from uniformly bounded-order ancestors without genealogy/branch loss.

It must be inherited from increasingly high-order ancestors or enter through a failure exit.

## 6. Exact mass transport on nested material sets

For any measurable initial material set `A`, incompressibility and Section 3 give

\[
\boxed{
E_t(X(A,t))
=
\int_A e^{2\Lambda(a;t_0,t)}|\Omega(a,t_0)|^2da.
}
\]

Take nested sets

\[
A_{in}\subset A_{out}.
\]

Define the multiplier oscillation on the outer set

\[
\operatorname{osc}_{A_{out}}\Lambda
:=
\sup_{A_{out}}\Lambda
-
\inf_{A_{out}}\Lambda.
\]

Then

\[
\boxed{
\frac{E_t(X(A_{in},t))}{E_t(X(A_{out},t))}
\ge
 e^{-2\operatorname{osc}_{A_{out}}\Lambda}
\frac{E_{t_0}(A_{in})}{E_{t_0}(A_{out})}.
}
\]

Thus material mass retention can deteriorate only through spatial oscillation of the accumulated scalar growth factor.

A spatially uniform `lambda(t)` changes total amplitude but leaves every material mass ratio exactly unchanged.

## 7. Flow distortion needed to compare Euclidean balls

M17-383 uses ordinary concentric balls rather than material images of balls.

Define the accumulated deformation

\[
K(t_0,t)
:=
\int_{t_0}^{t}\|\Sigma(s)\|_{L^\infty(\mathcal U_s)}ds
\]

on a material neighborhood `U_s` containing the relevant trajectories.

The distance evolution obeys the standard estimate

\[
 e^{-K}|a-b|
\le
|X(a,t)-X(b,t)|
\le
 e^K|a-b|.
\]

Hence for `x_t=X(a_0,t)`,

\[
\boxed{
X(B_{e^{-K}R}(a_0),t)
\subset
B_R(x_t)
\subset
X(B_{e^{K}R}(a_0),t).
}
\]

For the inner radius `theta R`,

\[
X(B_{e^{-K}\theta R}(a_0),t)
\subset
B_{\theta R}(x_t).
\]

Therefore

\[
E_t(B_R(x_t))
\le
E_t(X(B_{e^KR}(a_0),t)),
\]

while

\[
E_t(B_{\theta R}(x_t))
\ge
E_t(X(B_{e^{-K}\theta R}(a_0),t)).
\]

## 8. Quantitative finite-scale doubling transport inequality

Apply Section 6 to the nested initial balls

\[
B_{e^{-K}\theta R}(a_0)
\subset
B_{e^KR}(a_0).
\]

Let

\[
\mathcal O_\lambda
:=
\operatorname{osc}_{B_{e^KR}(a_0)}
\Lambda(a;t_0,t).
\]

Then

\[
\boxed{
\frac{E_t(B_R(x_t))}{E_t(B_{\theta R}(x_t))}
\le
 e^{2\mathcal O_\lambda}
\frac{
E_{t_0}(B_{e^KR}(a_0))
}{
E_{t_0}(B_{e^{-K}\theta R}(a_0))
}.
}
\]

Equivalently,

\[
\boxed{
\mathfrak D_\theta(x_t,R,t)
\le
\mathfrak D_{\theta e^{-2K}}
(a_0,e^KR,t_0)
+
2\mathcal O_\lambda.
}
\]

This is the central M17-384 inequality.

It is not a frequency-monotonicity theorem; it is an exact transport comparison based only on the CE-H multiplier law and bi-Lipschitz material deformation.

## 9. Split the multiplier oscillation into strain and coefficient parts

Because

\[
\lambda=\sigma+\nu\kappa,
\]

we have

\[
\boxed{
\mathcal O_\lambda
\le
\int_{t_0}^{t}
\operatorname{osc}_{\mathcal U_s}\sigma\,ds
+
\nu
\int_{t_0}^{t}
\operatorname{osc}_{\mathcal U_s}\kappa\,ds.
}
\]

On an M17-382 own-scale cell of radius comparable to `r`, the normalized coefficient-gradient compactness

\[
r^3|\nabla\kappa|\le G_*
\]

gives

\[
\operatorname{osc}\kappa
\lesssim
G_*r^{-2}.
\]

On one parabolic own-scale time window

\[
|I_r|
\lesssim
T_*\frac{r^2}{\nu},
\]

this yields

\[
\boxed{
\nu\int_{I_r}\operatorname{osc}\kappa\,dt
\lesssim
C T_*G_*.
}
\]

Therefore the coefficient part of the scalar multiplier cannot by itself create unbounded finite-scale doubling on a uniformly bounded number of own-scale time units while the M17-382 gradient compactness remains valid.

The remaining multiplier payer is the spatial strain-eigenvalue oscillation

\[
\int_{I_r}\operatorname{osc}\sigma\,dt.
\]

## 10. Relation to the strain-gradient channel

M17-361 proved on exact CE-H

\[
\boxed{|
\nabla\sigma|
\le
|\nabla\Sigma|.}
\]

Thus on a cell of diameter `O(r)`,

\[
\operatorname{osc}\sigma
\le
C r\|\nabla\sigma\|_{L^\infty}
\le
C r\|\nabla\Sigma\|_{L^\infty}.
\]

Accordingly, divergence of the strain-oscillation payer routes to a local high-strain-gradient/jet branch unless the geometry or domain needed for this comparison degenerates.

This does not yet convert the payer into a globally summable `L2` palinstrophy cost; M17-361 explicitly warns that normalized palinstrophy payments can still fall behind the inverse-record-scale ancestral firewall.

The present result is therefore a payer identification, not a global contradiction.

## 11. Exact dynamical split for the M17-383 branch

Suppose a sequence of M17-382 own-scale CE-H cells has

\[
\mathfrak N_\theta\to\infty.
\]

On a uniformly bounded own-scale time interval, M17-384 gives the following alternatives:

\[
\boxed{
\begin{aligned}
G_{local\ doubling/frequency\ decompactification}
\Longrightarrow{}&
G_{ancestral/inherited\ high\ doubling}\\
&\lor G_{material\ flow\ distortion}\\
&\lor G_{strain\text{-}growth\ spatial\ oscillation}\\
&\lor G_{r^3|\nabla\kappa|\ decompactification}\\
&\lor G_{CEH/interface/domain/genealogy\ loss}.
\end{aligned}
}
\]

For true pointwise vanishing order the statement is sharper:

\[
\boxed{
G_{high\ vanishing\ order\ at\ descendant}
\Longrightarrow
G_{same\ high\ order\ inherited\ from\ ancestor}
\lor
G_{CEH/flow/genealogy\ loss}.
}
\]

Thus high vanishing order is not an autonomous dynamically generated escape inside exact smooth CE-H.

## 12. Consequence for M17-298 localization

Combining M17-381--384, the CE-H localization debt is now

\[
\boxed{
\begin{aligned}
G_{M17\text{-}298}
\Longrightarrow{}&
H_{true\ scale\text{-}comparable\ packet}\\
&\lor G_{ancestral\ high\ doubling/vanishing\ order}\\
&\lor G_{material\ flow/strain\ distortion}\\
&\lor G_{strain\text{-}growth\ inhomogeneity}\\
&\lor G_{coefficient\ gradient\ decompactification}\\
&\lor G_{interface/domain/genealogy\ loss}.
\end{aligned}
}
\]

The original raw-`H2` cross-scale ownership problem remains closed on the exact CE-H coefficient-scale compact branch.

The newly isolated problem is whether inherited high doubling and the strain/deformation payers can be controlled by a certified cross-generation resource.

## 13. DSD audit role

The DSD contribution is only a dependency and representation audit:

- M17-383 showed that coefficient thickness is not solution-mass thickness;
- M17-384 asks which part of solution-mass thickness is material invariant and which part can change dynamically;
- exact CE-H shows that vanishing order is material, whereas finite-radius doubling is affected by material deformation and spatially nonuniform scalar growth.

No DSD axiom is inserted into the Navier--Stokes equations.

## 14. Audit verdict

**PASS — dynamical refinement.**

The M17-383 local-frequency exit is not one undifferentiated OPEN branch. Its asymptotic vanishing-order component is materially inherited, while finite-scale doubling growth must pay through flow distortion, strain-growth inhomogeneity, coefficient-gradient loss, or branch/genealogy loss.

The next highest-value task is to test whether the two finite-scale payers

\[
K_r
=
\int_{I_r}\|\Sigma\|_{L^\infty}dt
\]

and

\[
S_r
=
\int_{I_r}\operatorname{osc}_{\mathcal U_t}\sigma\,dt
\]

can be converted into an additive or Carleson-type quantity controlled by the already certified critical mass/raw-`H2`/palinstrophy ledgers, without violating the M17-307 inverse-record-scale firewall.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
