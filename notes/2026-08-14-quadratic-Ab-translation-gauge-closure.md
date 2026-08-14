# Quadratic `Ab` is a translation-gauge term

Date: 2026-08-14

Status: **EXACT FOR THE QUADRATIC-VELOCITY / FIRST-CHAOS-VORTICITY CORE. AFTER PASSING FROM THE GAUSSIAN-MEAN CENTER TO THE MATERIAL/TAYLOR CENTER, THE `Ab` MEAN SOURCE DISAPPEARS IDENTICALLY. COMBINED WITH GLOBAL TERMINAL TRACE COLLAPSE, THIS CLOSES THE BOUNDED-AFFINE LOW-HERMITE QUADRATIC-CORE MEAN-GENERATION LANE. GLOBAL REGULARITY NOT PROVED.**

## 1. Quadratic core in the Gaussian-mean frame

Work at one time in whitened Gaussian coordinates and write the exact quadratic velocity core as

\[
Q_i(z)=\frac12T_{i,jk}z_jz_k,
\qquad
T_{i,jk}=T_{i,kj},
\qquad
\nabla\cdot Q=0.
\]

Its Gaussian mean is

\[
\boxed{b=E_\gamma Q.}
\]

The self-consistent Gaussian-mean velocity frame uses

\[
\dot a_\gamma=E_\gamma u.
\]

For a quadratic Taylor expansion around the current center,

\[
u(a+z)=u(a)+Lz+Q(z),
\]

and because the Gaussian is centered,

\[
E_\gamma\nabla Q=0.
\]

Hence

\[
L=E_\gamma\nabla u=\nabla u(a).
\]

But

\[
E_\gamma u=u(a)+b,
\]

so

\[
\boxed{\dot a_\gamma=u(a)+b.}
\]

The residual velocity in this frame is therefore

\[
\boxed{w_\gamma=Q-b.}
\]

Its residual vorticity is

\[
\eta=\nabla\times Q=Az.
\]

## 2. Origin of the `Ab` term

The residual-residual vorticity nonlinearity is

\[
N_\omega
=(\eta\cdot\nabla)w_\gamma
-(w_\gamma\cdot\nabla)\eta.
\]

Because `eta=Az` is linear,

\[
(b\cdot\nabla)\eta=Ab.
\]

Thus

\[
\begin{aligned}
N_\omega
&=(\eta\cdot\nabla)Q
-(Q\cdot\nabla)\eta
+(b\cdot\nabla)\eta\\
&=P+Ab,
\end{aligned}
\]

where

\[
P=(Az\cdot\nabla)Q-AQ.
\]

Therefore

\[
\boxed{
Ab=(b\cdot\nabla)\eta
}
\]

is literally the constant-translation part of the transport term.

It is not a vortex-stretching creation term.

## 3. Material/Taylor center

Now choose the center to follow the actual fluid velocity at the center:

\[
\boxed{\dot a_m=u(a_m,t).}
\]

A time-dependent translation is an exact symmetry of force-free incompressible Navier--Stokes after the uniform frame acceleration is absorbed into a linear pressure term, so this is a legitimate gauge choice.

For an exact quadratic field expanded around `a_m`,

\[
u(a_m+z)=u(a_m)+L_mz+Q(z),
\]

with

\[
L_m=\nabla u(a_m)=E_\gamma\nabla u.
\]

The residual is now

\[
\boxed{w_m=Q.}
\]

The difference between the two center velocities is exactly

\[
\boxed{
\dot a_m-\dot a_\gamma=-b.
}
\]

Thus the material center moves relative to the Gaussian-mean center by precisely the velocity needed to cancel the constant residual `-b`.

## 4. Exact cancellation of `Ab`

In the material/Taylor frame the residual-residual vorticity source is

\[
N_\omega^{(m)}
=(\eta\cdot\nabla)Q
-(Q\cdot\nabla)\eta
=P.
\]

Hence

\[
\boxed{
N_\omega^{(m)}=P,
\qquad
J_{Ab}^{(m)}=0.
}
\]

Equivalently, when one transforms the Gaussian-mean frame to the material frame, the center-motion derivative contributes

\[
-(b\cdot\nabla)\eta=-Ab,
\]

which cancels the old `+Ab` term exactly.

Therefore

\[
\boxed{
J_{Ab}\text{ is a center-translation gauge contribution.}
}
\]

It can change the Gaussian mean attached to one chosen moving center, but it does not represent creation of vorticity magnitude along a material center.

## 5. Gaussian mean equals point vorticity for the quadratic core in the material frame

Since

\[
\eta(z)=Az
\]

is centered,

\[
E_\gamma\eta=0.
\]

Therefore, for the quadratic core,

\[
\boxed{
\bar\Omega_\gamma
=E_\gamma\Omega
=\Omega(a_m,t).
}
\]

Thus the tracked Gaussian mean in the material/Taylor gauge is exactly the point vorticity on the center trajectory at this order.

This is the correct quantity for distinguishing genuine amplification from mere passage of a linear profile across an observation center.

## 6. The only quadratic-core mean source left is the trace source

In the material frame,

\[
J_{\rm core}^{(m)}=E_\gamma P.
\]

The exact mean-trace/second-chaos identity gives

\[
\boxed{
|E_\gamma P|
\le
\sqrt{\frac32}\,\|N_{\omega,2}\|_{L^2(\gamma)}.
}
\]

The full-terminal trace telescoping argument, using

\[
B(\tau)\lesssim\min\{m,\tau\},
\]

already proves on the bounded-condition, bounded-accumulated-affine branch that over the complete natural mean-creation interval

\[
\boxed{
\left|\int_0^{c/m}J_{\rm tr}(\tau)d\tau\right|
\lesssim
\sqrt m\,(1+|\log m|)
\to0.
}
\]

Hence an asymptotically pure quadratic/first-chaos core cannot produce an order-one material-center mean-vorticity change.

## 7. Bounded affine inheritance cannot replace the missing source

At the previous adaptive first-hitting checkpoint,

\[
\|\Omega\|_\infty\le q^{-1},
\qquad
q\to\infty.
\]

On the bounded accumulated-affine branch, the homogeneous Cauchy/affine propagator has uniformly bounded operator norm, so pure affine inheritance remains

\[
O_K(q^{-1})=o(1).
\]

Pure heat contracts.

The frozen mean-vorticity linear coupling is skew in whole-space `L2` and is a redistribution mechanism, not an averaged material-center creation term.

Therefore an order-one terminal material-center vorticity cannot arise from

1. bounded affine inheritance;
2. heat;
3. the quadratic `Ab` term;
4. the quadratic trace term.

## 8. Low-Hermite branch closure

Suppose a surviving bounded-affine terminal episode has

\[
B\to0
\]

and the residual state is asymptotically quadratic/first-chaos in the sense that all higher-Hermite and translation/frame remainders contribute `o(1)` to the terminal material-center mean action.

Then the preceding sections imply

\[
\boxed{
\Delta\Omega_{\rm material\ center}=o(1),
}
\]

contradicting the adaptive first-hitting change from `O(q^-1)` to order one.

Thus

\[
\boxed{
\text{bounded affine}
+\text{low Hermite}
+\text{controlled moving-center remainder}
\Longrightarrow
\text{no surviving amplification step}.
}
\]

## 9. What a survivor must now do

A surviving bounded-affine cascade must leave the quadratic-core regime through at least one typed channel:

\[
\boxed{
\begin{array}{ll}
\text{H.}&\text{higher-Hermite / curvature surplus},\\
\text{T.}&\text{nontrivial translation/shell import beyond the quadratic gauge},\\
\text{F.}&\text{frame/covariance degeneration},\\
\text{A.}&\text{unbounded accumulated symmetric-affine strain},\\
\text{V.}&\text{viscous higher-derivative / palinstrophy concentration}.
\end{array}
}
\]

`Ab` is removed from this list as an independent physical amplification mechanism.

## 10. Interpretation

The old Gaussian-mean frame was optimal for least-squares cancellation,

\[
E_\gamma r=0,
\qquad
E_\gamma\nabla r=0,
\]

but that convenience makes translation of a linear vorticity profile appear as a mean source.

The material/Taylor frame sacrifices `E_gamma r=0` but preserves

\[
E_\gamma\nabla r=0
\]

for the quadratic core and separates the physically relevant question:

> did the vorticity on the tracked fluid center grow, or did a pre-existing profile merely pass through the observation center?

At quadratic order the answer is exact: `Ab` belongs to the second category.

Status: **QUADRATIC `Ab` ESCAPE REMOVED AS TRANSLATION GAUGE / FULL TERMINAL TRACE ACTION IS `o(1)` / BOUNDED-AFFINE LOW-HERMITE QUADRATIC-CORE AMPLIFICATION BRANCH CLOSED / REMAINING SURVIVOR MUST ACTIVATE HIGHER HERMITE, NONQUADRATIC TRANSPORT, FRAME DEGENERATION, LARGE AFFINE STRAIN, OR HIGHER-DERIVATIVE VISCOSITY / GLOBAL REGULARITY NOT PROVED.**
