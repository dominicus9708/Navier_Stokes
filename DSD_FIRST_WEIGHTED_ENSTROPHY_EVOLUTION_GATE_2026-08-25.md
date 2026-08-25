# DSD First Weighted-Enstrophy Evolution Gate

Date: 2026-08-25

Status: **EXACT WEIGHTED-MOMENT IDENTITY / DIFFUSION FAVORABLE / STRAIN-DRIVEN GROWTH STILL PERMITS THE CRITICAL CONVEYOR / GLOBAL REGULARITY UNPROVED.**

## 1. Motivation

The permanent-export log-radius conveyor identified in

`DSD_ESCAPING_CRITICAL_TAIL_LOG_RADIUS_CONVEYOR_2026-08-25.md`

is invisible to the unweighted enstrophy budget but is counted without radial decay by

\[
\mathcal M_1^\Omega
=\int |Y||\Omega|^2dY.
\]

Because

\[
\mathcal M_1^\Omega
=\nu^{-2}\int |x-X||\omega|^2dx,
\]

it is natural to ask whether the physical first weighted-enstrophy moment is uniformly controlled by the smooth Navier--Stokes dynamics.

## 2. Material-centered weighted moment

Let \(X(t)\) be a material trajectory,

\[
\dot X(t)=u(X(t),t).
\]

Set

\[
r(x,t)=|x-X(t)|,
\qquad
M_1(t)=\int_{\mathbb R^3}r|\omega|^2dx.
\]

For smooth rapidly decaying solutions all integrations below are legitimate; a regularization \(r_\varepsilon=(r^2+\varepsilon^2)^{1/2}\) may be inserted and then removed.

## 3. Exact evolution identity

The vorticity amplitude-square equation is

\[
(\partial_t+u\cdot\nabla)|\omega|^2
=
2\omega\cdot S\omega
+\nu\Delta|\omega|^2
-2\nu|\nabla\omega|^2.
\]

Since

\[
\partial_t r=-\dot X\cdot n,
\qquad
\nabla r=n,
\qquad
\Delta r=\frac2r
\]

away from the center, integration by parts gives

\[
\boxed{
\begin{aligned}
M_1'(t)
={}&
\int (u-\dot X)\cdot n\,|\omega|^2dx\\
&+2\int r\,\omega\cdot S\omega\,dx\\
&-2\nu\int r|\nabla\omega|^2dx
+2\nu\int \frac{|\omega|^2}{r}dx.
\end{aligned}
}
\]

This is exact.

## 4. Weighted Hardy closes the diffusion pair

The weighted Hardy inequality in three dimensions with weight \(r\) is

\[
\boxed{
\int \frac{|f|^2}{r}dx
\le
\int r|\nabla f|^2dx.
}
\]

Apply it componentwise to \(\omega\). Then

\[
-2\nu\int r|\nabla\omega|^2dx
+2\nu\int\frac{|\omega|^2}{r}dx
\le0.
\]

Thus viscosity cannot drive growth of the critical first moment.

Status: **PROVED.**

## 5. Radial transport depends only on strain

Because \(\dot X=u(X,t)\),

\[
(u(x)-\dot X)\cdot n
=
\int_0^1
n\cdot\nabla u(X+\theta rn)\,(rn)
\,d\theta.
\]

Decompose

\[
\nabla u=S+A,
\qquad A^T=-A.
\]

Since

\[
n\cdot A n=0,
\]

one obtains

\[
|(u-\dot X)\cdot n|
\le r\|S(t)\|_{L^\infty}.
\]

The stretching term satisfies

\[
2r\,\omega\cdot S\omega
\le
2\|S(t)\|_\infty r|\omega|^2.
\]

Therefore

\[
\boxed{
M_1'(t)
\le
3\|S(t)\|_\infty M_1(t).
}
\]

Consequently

\[
\boxed{
M_1(t)
\le
M_1(t_0)
\exp\!\left(
3\int_{t_0}^t\|S(s)\|_\infty ds
\right).
}
\]

## 6. Why this does not yet close the conveyor

On one dynamic first-hitting stage, write

\[
S=W_j\Sigma,
\qquad dt=W_j^{-1}d\tau_j.
\]

Then

\[
\int_{I_j}\|S\|_\infty dt
=
\int_{I_j}\|\Sigma\|_\infty d\tau_j.
\]

On the bounded pure corridor this is bounded by an order-one stage constant, but it does not tend to zero with \(j\).

Hence over \(N\) stages the exact estimate permits

\[
M_1(t_N)
\lesssim
M_1(t_0)e^{CN}.
\]

The critical export conveyor only forces roughly

\[
M_1(t_N)\gtrsim cN
\]

when each geometrically separated critical shell contributes an order-one weighted-enstrophy amount.

Therefore the available upper estimate is far too weak to contradict the conveyor.

Status: **NO CLOSURE.**

## 7. Center mismatch

The preceding identity is cleanest for a material center.

If the first-hitting recurrence center is not comparable to a material trajectory, the mismatch is already a center-turnover/material-export contribution in the existing T ledger.

Therefore this note should be used on the no-center-turnover branch only; large center mismatch is not silently ignored.

## 8. Structural interpretation

The first weighted-enstrophy moment is exactly critical under the first-hitting rescaling and exactly neutral with respect to the Leray dilation.

Its evolution confirms the same endpoint structure as the log-radius calculation:

- viscosity is favorable;
- rigid rotation is irrelevant to radial growth;
- only strain/transport can amplify the moment;
- the standard first-hitting corridor allows enough cumulative strain to support logarithmically many critical shells.

Thus a uniform bound for \(M_1\) would be a genuinely new rigidity input, not a consequence of the present energy/enstrophy estimates.

## 9. Audit verdict

### PROVED

\[
\boxed{
M_1'
\le
3\|S\|_\infty M_1.
}
\]

with the diffusion pair nonpositive by weighted Hardy.

### IMPORTANT NEGATIVE RESULT

The standard bounded-stage strain ledger does not imply a uniform first weighted-enstrophy bound; it permits growth much faster than the linear shell accumulation required by permanent export.

### OPEN

A stronger cancellation, geometric sign condition, return theorem, or independent scale-critical bound is still required.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
