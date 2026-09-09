# DSD M17-458 — Finite palinstrophy ancestry forces asymptotically exact positive/negative kappa-weighted enstrophy cancellation on persistent baseline diffuse records

Date: 2026-09-09  
Canonical ID: **M17-458**

Status: **ACTIVE SIGN-BALANCE RIGIDITY THEOREM / M17-455--457 TEMPORAL REFINEMENT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Exact sign identity

On whole-space exact CE-H,

\[
P_R(t)
:=
\|\nabla\Omega_R(t)\|_2^2
=
K_{-,R}(t)-K_{+,R}(t),
\]

where

\[
K_{\pm,R}(t)
:=
\int (\kappa_R)_\pm\rho_R^2dx.
\]

Thus

\[
\boxed{
0\le K_{-,R}-K_{+,R}=P_R.
}
\]

M17-455 shows that on a baseline-size positive-kappa diffuse carrier, `K_+` and hence `K_-` have fixed positive lower bounds on every retained good state.

## 2. Parent-time record window

Use the parent-normalized record window `J_R` from the late-loop packing architecture, with

\[
|J_R|\asymp c_TR^2.
\]

Define the palinstrophy ancestry charge of that record

\[
\boxed{
a_R
:=
R^{-1}
\int_{J_R}P_R(t)dt.
}
\]

M17-307 and finite-overlap genealogy give

\[
\boxed{
\sum_m a_{R_m}<\infty.
}
\]

In particular,

\[
\boxed{a_{R_m}\to0.}
\]

## 3. Average sign imbalance on the full record

Because

\[
\int_{J_R}P_Rdt=Ra_R,
\]

one has

\[
\boxed{
\frac1{|J_R|}
\int_{J_R}
(K_{-,R}-K_{+,R})dt
\lesssim
\frac{a_R}{R}.
}
\]

Along the record sequence,

\[
\boxed{
\overline{K_- - K_+}^{\,J_R}
=o(R^{-1}).
}
\]

Thus the two order-one weighted sign populations must cancel much more accurately than their individual sizes.

## 4. Good-time subset

Let `G_R subset J_R` be the baseline diffuse positive-kappa good-time set and assume

\[
|G_R|\ge\beta_*|J_R|
\]

for a fixed `beta_*>0`.

Since `P_R>=0`,

\[
\int_{G_R}P_Rdt
\le
\int_{J_R}P_Rdt
=Ra_R.
\]

Therefore

\[
\boxed{
\frac1{|G_R|}
\int_{G_R}(K_{-,R}-K_{+,R})dt
\lesssim
\frac{a_R}{\beta_*R}.
}
\]

If M17-455 gives on `G_R`

\[
K_{+,R}\ge k_*>0,
\]

then also `K_- >= k_*`, and the relative average imbalance obeys

\[
\boxed{
\frac{
\int_{G_R}(K_- -K_+)dt
}{
\int_{G_R}(K_-+K_+)dt
}
\lesssim
\frac{a_R}{R}.
}
\]

Hence the relative cancellation error tends to zero at least at the record-inverse scale times the summable ancestry charge.

## 5. Chebyshev concentration in time

For any threshold `epsilon_R>0`,

\[
\left|
\{t\in G_R:P_R(t)\ge\epsilon_R\}
\right|
\le
\frac{Ra_R}{\epsilon_R}.
\]

Divide by `|G_R| >= cR^2`:

\[
\boxed{
\frac1{|G_R|}
\left|
\{t\in G_R:P_R(t)\ge\epsilon_R\}
\right|
\lesssim
\frac{a_R}{R\epsilon_R}.
}
\]

For example, choosing

\[
\epsilon_R=R^{-1/2}
\]

gives

\[
\boxed{
\operatorname{Frac}_{G_R}
\{P_R\ge R^{-1/2}\}
\lesssim
a_RR^{-1/2}\to0.
}
\]

Thus on almost all good time, the positive and negative coefficient moments are not merely comparable; their difference is small.

More generally any `epsilon_R` satisfying

\[
R\epsilon_R/a_R\to\infty
\]

has asymptotically full good-time concentration on

\[
0\le K_- -K_+<\epsilon_R.
\]

## 6. Consequence for M17-454 thick negative cores

If a mesoscopically thick negative core with fixed enstrophy mass existed on a fixed positive fraction of `G_R`, M17-454 would give `P_R>=c_*>0` there.

Section 5 shows that such times have vanishing fraction because

\[
\operatorname{Frac}_{G_R}\{P_R\ge c_*\}
\lesssim
\frac{a_R}{R}\to0.
\]

This recovers M17-454's incompatibility in a sharper temporal form: the finite palinstrophy ledger forces almost all baseline diffuse good-time states into a **near-perfect sign-cancellation regime**.

## 7. What this rigidity means

At typical retained good times,

\[
K_-(t)\sim K_+(t)\sim O(1),
\]

while

\[
K_-(t)-K_+(t)=P_R(t)\to0
\]

in time-density sense.

Thus the survivor cannot be viewed as a dominant negative compensation correcting a smaller positive population. It requires two substantial weighted sign populations with increasingly precise cancellation.

Any mechanism that causes order-one drift in the ratio `K_-/K_+` over a positive fraction of parent time would activate the favorable palinstrophy ancestry ledger and close that subbranch.

## 8. New narrow target

The exact dynamics of

\[
A_R:=K_-+K_+
=
\int|\kappa_R|\rho_R^2dx
\]

and

\[
S_R:=K_+-K_-
=
\int\kappa_R\rho_R^2dx
=-P_R
\]

should now be compared.

The absolute moment `A_R` is sensitive to zero-level transfer. Formally the Kato identity

\[
L_\rho|\kappa|
=
\operatorname{sgn}(\kappa)L_\rho\kappa
+2\delta(\kappa)|\nabla\kappa|^2
\]

shows that zero-level coefficient diffusion enters `dA_R/dt` with a definite sign.

This is the next canonical route: determine whether maintaining `A_R=O(1)` while `S_R=o(1/R)` forces nonsummable zero-current/source-return activity.

## 9. Audit verdict

**PASS — the diffuse sign-compensation survivor is quantitatively rigid.**

Finite ancestral palinstrophy forces positive and negative kappa-weighted enstrophy moments to cancel asymptotically exactly on almost all persistent baseline good-time states. The next unresolved mechanism is how such cancellation can be dynamically maintained in the presence of coefficient diffusion and zero-level transfer.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
