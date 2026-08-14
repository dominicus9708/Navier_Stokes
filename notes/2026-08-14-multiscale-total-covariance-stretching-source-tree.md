# Multiscale law of total covariance for the residual stretching source

Date: 2026-08-14

Status: **EXACT GAUSSIAN CONDITIONAL-COVARIANCE RECURSION. A PARENT RESIDUAL STRETCHING SOURCE CAN ONLY DESCEND TO CHILD RESIDUAL SOURCES OR BE CONVERTED INTO A BETWEEN-SCALE COVARIANCE INCREMENT. THERE IS NO THIRD HIGH-HERMITE SOURCE CHANNEL. GLOBAL REGULARITY NOT PROVED.**

## 1. Parent Gaussian as a child-mixture

Let the parent covariance split as

\[
\Sigma_p=\Sigma_c+C,
\qquad
C\succ0.
\]

Write

\[
X=Y+Z,
\]

with independent

\[
Y\sim N(0,C),
\qquad
Z\sim N(0,\Sigma_c).
\]

Then `X~N(0,Sigma_p)`.

For a fixed physical time and parent center `a`, evaluate the fields at

\[
a+X=a+Y+Z.
\]

Conditioning on `Y` means observing a child Gaussian of covariance `Sigma_c` centered at `a+Y`.

## 2. Child means and child residual source

Define the child conditional means

\[
\boxed{
S_c(Y)=E_Z[S(a+Y+Z)],
}
\]

\[
\boxed{
\Omega_c(Y)=E_Z[\Omega(a+Y+Z)].
}
\]

Define the child residual stretching source

\[
\boxed{
J_c(Y)
=E_Z[
(S-S_c(Y))(\Omega-\Omega_c(Y))
].
}
\]

The parent means are

\[
S_p=E_Y S_c(Y),
\qquad
\Omega_p=E_Y\Omega_c(Y).
\]

The parent residual source is

\[
\boxed{
J_p
=E_X[(S-S_p)(\Omega-\Omega_p)].
}
\]

## 3. Exact source law of total covariance

Expand

\[
S-S_p
=(S-S_c)+(S_c-S_p),
\]

\[
\Omega-\Omega_p
=(\Omega-\Omega_c)+(\Omega_c-\Omega_p).
\]

Conditional means make the cross terms vanish. Therefore

\[
\boxed{
J_p
=E_Y[J_c(Y)]
+J_{p\to c}^{\rm between},
}
\]

where

\[
\boxed{
J_{p\to c}^{\rm between}
:=
E_Y[(S_c-S_p)(\Omega_c-\Omega_p)].
}
\]

This is the exact law of total covariance for the Navier--Stokes residual stretching source.

Thus parent mean stretching has only two origins:

1. actual residual stretching inside child windows;
2. covariance between the child mean strain and child mean vorticity across child centers.

## 4. Between-source is bounded by the exact between-scale variance increment

Define the child-mean between-scale variances

\[
\Delta_S
:=E_Y|S_c-S_p|^2,
\]

\[
\Delta_\omega
:=E_Y|\Omega_c-\Omega_p|^2.
\]

Then

\[
|J_{p\to c}^{\rm between}|
\le
\sqrt{\Delta_S\Delta_\omega}.
\]

Define the four-channel between-scale increment

\[
\boxed{
\Delta B_{p\to c}
:=
\Delta_S+\frac12\Delta_\omega.
}
\]

The elementary optimization

\[
\sqrt{ab}
\le
\frac1{\sqrt2}\left(a+\frac12b\right)
\]

gives

\[
\boxed{
|J_{p\to c}^{\rm between}|
\le
\frac1{\sqrt2}\Delta B_{p\to c}.
}
\]

Thus the between-scale source has exactly the same sharp four-channel coefficient as the residual source itself.

## 5. Exact total-variance recursion

The scalar/matrix law of total variance gives

\[
V_{S,p}
=E_Y[V_{S,c}(Y)]+\Delta_S,
\]

\[
V_{\omega,p}
=E_Y[V_{\omega,c}(Y)]+\Delta_\omega.
\]

Therefore

\[
\boxed{
B_p
=E_Y[B_c(Y)]
+\Delta B_{p\to c}.
}
\]

This is the same between-scale increment already used in the Gaussian scale-packing route.

Combining source and variance recursions,

\[
\boxed{
J_p
=E_Y[J_c(Y)]
+J_{p\to c}^{\rm between},
\qquad
|J_{p\to c}^{\rm between}|
\le\Delta B_{p\to c}/\sqrt2.
}
\]

## 6. Iterate down a nested Gaussian tree

For a nested covariance chain

\[
\Sigma_0\succ\Sigma_1\succ\cdots\succ\Sigma_N,
\]

iterated conditional expectation gives schematically

\[
\boxed{
J_0
=E[J_N]
+\sum_{k=0}^{N-1}
E[J_{k\to k+1}^{\rm between}].
}
\]

Meanwhile the nonnegative variance increments telescope:

\[
\boxed{
B_0
=E[B_N]
+\sum_{k=0}^{N-1}E[\Delta B_{k\to k+1}].
}
\]

Hence

\[
\boxed{
\sum_{k=0}^{N-1}
E|J_{k\to k+1}^{\rm between}|
\le
\frac1{\sqrt2}
\sum_{k=0}^{N-1}E[\Delta B_{k\to k+1}]
\le
\frac1{\sqrt2}B_0
}
\]

when the source directions are estimated by absolute values before averaging.

There is therefore no hidden multiplicative source gain from descending through many scales.

## 7. Interpretation of the high-Hermite branch

A high-Hermite parent state is a state whose variation is unresolved at the parent Gaussian scale. The recursion shows that its mean stretching action must do one of two things as resolution increases:

### H1. Descend

A fixed fraction remains an actual child residual source and moves to a smaller spatial scale.

### H2. Convert to between-scale mismatch

A fixed fraction becomes covariance between child mean strain and child mean vorticity. That action is bounded by the already positive, exactly telescoping between-scale variance increment.

No third `high-chaos mean source` exists independently of these two mechanisms.

## 8. End of descent

If H1 repeats, fixed-ratio curvature descent reaches, after `O(log R)` generations, either

1. a low-Hermite / low-curvature child state; or
2. an endpoint derivative-concentration event.

The low-Hermite bounded-affine quadratic material-center branch has now been closed:

- `Ab` is translation gauge;
- full-terminal trace action is `o(1)`;
- exact SO(2) quadratic resonance still forces second chaos.

Therefore a surviving H1 chain cannot terminate cheaply in a pure quadratic/first-chaos source. It must activate a nonquadratic derivative event before or at the end of descent.

If H2 dominates instead, its source action is paid by the between-scale variance ledger and is subject to fixed-time spatial-scale packing.

## 9. Remaining dynamical issue

At one fixed physical time, between-scale increments telescope exactly and low-curvature active states satisfy the existing scale-Carleson estimate.

The unresolved issue is temporal reuse: the Navier--Stokes evolution may rebuild between-scale variance after viscosity/transport has moved or erased the previous state.

Therefore the high-Hermite endgame is sharpened to

\[
\boxed{
\text{repeated regeneration of between-scale variance}
\quad\text{or}\quad
\text{endpoint derivative concentration}.
}
\]

The former is a scale-time replenishment problem; the latter is already the derivative/palinstrophy branch.

Status: **HIGH-HERMITE MEAN SOURCE REDUCED EXACTLY TO CHILD-SOURCE DESCENT OR POSITIVE BETWEEN-SCALE VARIANCE / LOW-HERMITE TERMINUS CLOSED / REMAINING H-BRANCH = SCALE-TIME VARIANCE REGENERATION OR ENDPOINT HIGH-DERIVATIVE CONCENTRATION / GLOBAL REGULARITY NOT PROVED.**
