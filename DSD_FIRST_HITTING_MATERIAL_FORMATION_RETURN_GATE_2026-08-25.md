# DSD first-hitting material formation / dynamic-channel return gate

Date: 2026-08-25

Status: **FINITE LOCAL FORMATION DEFECT PROVED / MATERIAL-ENSTROPHY CHANNEL RETURN PROVED / AUXILIARY DERIVATIVE-LADDER SURVIVOR RECLASSIFIED / GLOBAL BUDGET CLOSURE NOT DERIVED / GLOBAL REGULARITY UNPROVED.**

This note pushes the DSD route without promoting R1 descriptor recurrence to material recurrence. The key observation is simpler: the definition of successive first-hitting amplitudes itself creates a finite, gauge-safe formation difference when an earlier physical state is represented in a later first-hitting base.

Throughout, let

\[
W_j=q^jW_0,\qquad q>1,
\]

and

\[
r_j=\left(\frac\nu{W_j}\right)^{1/2}.
\]

Choose a maximum point `X_j` at the first-hitting time `t_j`, and normalize

\[
\Omega_j(y)
:=\frac{\omega(X_j+r_jy,t_j)}{W_j}.
\]

Thus

\[
\|\Omega_j\|_\infty=1.
\]

## 1. Earlier state represented in a future base

Fix a finite generation gap `k>=1` and put

\[
n=j+k.
\]

Represent the earlier physical vorticity at time `t_j` using the later center, radius, and amplitude base:

\[
\boxed{
\widehat\Omega_{j\to n}(y)
:=\frac{\omega(X_n+r_ny,t_j)}{W_n}.
}
\]

Because `t_j` is a first-hitting time and the running vorticity maximum at that time is `W_j`, one has everywhere

\[
|\omega(x,t_j)|\le W_j.
\]

Hence

\[
\boxed{
\|\widehat\Omega_{j\to n}\|_\infty
\le\frac{W_j}{W_n}=q^{-k}.
}
\]

This conclusion is independent of center displacement. No genealogy assumption is used.

Status: **PROVED.**

## 2. Future analytic core gives a finite local formation defect

The first-hitting analyticity corridor gives a fixed normalized radius `r_a>0`, independent of the late stage, such that

\[
\boxed{
|\Omega_n(y)|\ge\frac12
\qquad(y\in B_{r_a}(0)).
}
\]

Choose once and for all a finite integer

\[
\boxed{
k_0:=\min\{k\in\mathbb N:q^{-k}\le1/4\}.}
\]

Then for every `j`, with `n=j+k_0`, define the finite formation defect

\[
D_{j,k_0}(y):=\Omega_n(y)-\widehat\Omega_{j\to n}(y).
\]

On the fixed ball `B_{r_a}`,

\[
|D_{j,k_0}(y)|
\ge|\Omega_n(y)|-|\widehat\Omega_{j\to n}(y)|
\ge\frac14.
\]

Therefore

\[
\boxed{
\|D_{j,k_0}\|_{L^2(B_{r_a})}
\ge
c_a:=\sqrt{\frac\pi{12}}\,r_a^{3/2}>0.
}
\]

This is an order-one **finite local describability difference** created over every `k_0`-generation first-hitting block.

It is not R1 recurrence, not a limit object, and not a material-identity assumption.

Status: **PROVED.**

## 3. Convert the future occupied ball into a material cell

At the later time `t_n`, define the physical occupied ball

\[
A_n:=B_{r_ar_n}(X_n).
\]

Let `Phi(t;t_n,x)` be the smooth backward flow map on the pre-singular interval and define the same material cell at earlier times by

\[
\boxed{
A(t):=\Phi(t;t_n,A_n),
\qquad t\in[t_j,t_n].
}
\]

Incompressibility gives

\[
\boxed{|A(t)|=|A_n|=\frac{4\pi}{3}r_a^3r_n^3.}
\]

At the final time, analyticity gives

\[
|\omega(x,t_n)|\ge\frac12W_n
\qquad(x\in A_n).
\]

At the initial time, the first-hitting property gives everywhere, and hence on `A(t_j)`,

\[
|\omega(x,t_j)|\le W_j=q^{-k_0}W_n\le\frac14W_n.
\]

Thus the same formed material cell has strictly larger enstrophy at the later endpoint.

## 4. Quantitative material-enstrophy formation gap

Define

\[
\mathcal E_A(t)
:=\frac12\int_{A(t)}|\omega(x,t)|^2dx.
\]

At the later endpoint,

\[
\mathcal E_A(t_n)
\ge
\frac18W_n^2|A_n|.
\]

At the earlier endpoint,

\[
\mathcal E_A(t_j)
\le
\frac12q^{-2k_0}W_n^2|A_n|
\le
\frac1{32}W_n^2|A_n|.
\]

Therefore

\[
\boxed{
\mathcal E_A(t_n)-\mathcal E_A(t_j)
\ge
\frac3{32}W_n^2|A_n|.
}
\]

Using

\[
W_n=\frac\nu{r_n^2},
\]

we obtain the physical-scale lower bound

\[
\boxed{
\mathcal E_A(t_n)-\mathcal E_A(t_j)
\ge
c_{a,E}\frac{\nu^2}{r_n},
\qquad
c_{a,E}:=\frac\pi8r_a^3.
}
\]

Equivalently, after multiplication by the natural critical length `r_n`, every such finite formation event carries an order-one normalized material-enstrophy gap:

\[
\boxed{
\frac{r_n}{\nu^2}
\left[\mathcal E_A(t_n)-\mathcal E_A(t_j)\right]
\ge c_{a,E}>0.
}
\]

Status: **PROVED.**

## 5. Exact material enstrophy identity

Because `A(t)` is a material region, the advective transport term is absorbed by the moving domain. The vorticity equation gives

\[
\boxed{
\frac{d}{dt}\mathcal E_A(t)
=
\int_{A(t)}(\omega\cdot\nabla u)\cdot\omega\,dx
-\nu\int_{A(t)}|\nabla\omega|^2dx
+\nu\int_{\partial A(t)}\omega\cdot\partial_n\omega\,dS.
}
\]

The antisymmetric part of `nabla u` does not contribute to the quadratic contraction, so the stretching term may be written with the strain tensor `S`:

\[
(\omega\cdot\nabla u)\cdot\omega
=\omega^TS\omega.
\]

This identity contains only actual vorticity-dynamic channels:

1. bulk vortex stretching;
2. bulk viscous dissipation;
3. viscous flux through the moving material boundary.

There is no auxiliary derivative-order ladder in the identity.

Status: **PROVED for smooth pre-singular material cells.**

## 6. Dynamic Channel-Return Gate

Integrating over `[t_j,t_n]` and dropping the non-positive bulk dissipation term from the upper bound gives

\[
\begin{aligned}
\mathcal E_A(t_n)-\mathcal E_A(t_j)
\le{}&
\int_{t_j}^{t_n}\int_{A(t)}|S||\omega|^2\,dxdt\\
&+\nu\int_{t_j}^{t_n}\int_{\partial A(t)}
(\omega\cdot\partial_n\omega)_+\,dSdt.
\end{aligned}
\]

Define

\[
\mathcal X_{j,n}
:=\int_{t_j}^{t_n}\int_{A(t)}|S||\omega|^2\,dxdt,
\]

and

\[
\mathcal B_{j,n}
:=\nu\int_{t_j}^{t_n}\int_{\partial A(t)}
(\omega\cdot\partial_n\omega)_+\,dSdt.
\]

Then

\[
\boxed{
\mathcal X_{j,n}+\mathcal B_{j,n}
\ge
c_{a,E}\frac{\nu^2}{r_n}.
}
\]

Hence at least one true dynamic channel obeys

\[
\boxed{
\mathcal X_{j,n}
\ge\frac{c_{a,E}}2\frac{\nu^2}{r_n}
\quad\lor\quad
\mathcal B_{j,n}
\ge\frac{c_{a,E}}2\frac{\nu^2}{r_n}.
}
\]

This is the finite DSD **Dynamic Channel-Return Gate (DCRG)**:

\[
\boxed{
\text{first-hitting finite formation}
\Longrightarrow
\text{bulk stretching charge}
\lor
\text{viscous boundary-influx charge}.
}
\]

Status: **PROVED.**

## 7. Consequence for the derivative-ladder branch

The previous finite derivative ladders arose only as Taylor/persistence certificates used to decide whether a large local derivative occupies enough space to create an integral cost.

The present material identity shows that they are not primitive source channels of the actual first-hitting formation event. Regardless of how many auxiliary derivative orders are introduced in a spatial persistence proof, the order-one material-enstrophy formation gap must return to one of the two direct positive supply channels above.

Therefore the earlier open structural CRG question

\[
\text{finite derivative ladder}\to?\to\text{actual dynamic channel}
\]

is resolved at the level of channel typing:

\[
\boxed{
\text{auxiliary derivative ladder is not an independent terminal mechanism.}
}
\]

It may still be needed to estimate `mathcal X` or `mathcal B`, but it no longer needs to be treated as a separate physical survivor.

Status: **PROVED AS A DSD DYNAMICAL-CHANNEL RECLASSIFICATION.**

## 8. What DCRG does not yet close

The lower bound scales as

\[
\nu^2/r_n.
\]

This is large instantaneously in physical units, but it is an **integrated channel charge**, not ordinary Leray dissipation. Neither

\[
\int|S||\omega|^2
\]

nor the positive material-boundary vorticity flux has yet been shown to possess a finite global spacetime budget controlled by the basic energy inequality.

Moreover, first-hitting blocks overlap if every `j` is used. One may select disjoint `k_0`-spaced blocks, but a contradiction still requires a finite global budget for the selected positive charges or a cancellation/transfer theorem showing that repeated boundary influx cannot be freely recycled.

Therefore

\[
\boxed{
\text{DCRG is proved, but the Budget-Closure Gate (BCG) is NOT DERIVED.}
}
\]

## 9. New compressed frontier

After the DSD finite-formation audit, the previous local tree

\[
\text{palinstrophy packet}\lor\text{finite derivative ladder}
\]

is no longer the primitive dynamical frontier.

Every sufficiently separated first-hitting formation block produces

\[
\boxed{
\text{bulk vortex stretching}
\lor
\text{viscous material-boundary influx}.
}
\]

Thus the next proof obligation is not to climb derivative order. It is to test whether these two positive supply channels can be globally recycled across an infinite first-hitting tower without violating a formed finite budget or an exact cancellation law.

Call this the

\[
\boxed{\text{Budget-Closure Gate (BCG)}.}
\]

Current status:

\[
\boxed{\text{BCG: NOT DERIVED.}}
\]

## 10. Audit verdict

### PROVED

- every fixed finite `k_0` with `q^{-k_0}<=1/4` gives an order-one local first-hitting formation defect;
- the future analytic core pulled backward as a material cell has an order-one normalized enstrophy increase;
- material advection disappears from the cell budget;
- the increase must be supplied by bulk vortex stretching or positive viscous boundary influx;
- auxiliary derivative ladders are not independent terminal dynamical mechanisms.

### NOT DERIVED

- a finite global budget for the positive stretching charge;
- a finite global budget for positive material-boundary vorticity influx;
- a no-recycling theorem across infinitely many first-hitting blocks;
- global regularity.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
