# M19-299 — At the unconditioned energy extremum the depth channel is exactly a production-slope covariance, and endpoints alone do not fix its sign

**Date:** 2026-09-16  
**Status:** ACTIVE DYNAMIC-CORE AUDIT / CONDITIONED DEPTH SIGN CLASSIFIED AS COVARIANCE / ENDPOINT-ONLY CLOSURE NO-GO

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Unconditioned extremizing depth

M19-269 selects a finite depth `z_E` at which the unconditioned q-averaged spherical energy satisfies

\[
\boxed{
\mathscr E'(z_E)=0,
}
\]

where

\[
\mathscr E(z)=\langle e(z)\rangle.
\]

M19-297/298 define the production-conditioned profile

\[
\mathscr E_m(z)=\langle m_h e(z)\rangle
\]

and

\[
Z_m(z)=-\mathscr E_m'(z).
\]

## 2. Exact covariance identity at z_E

Because `m_h` is a state observable independent of wedge depth,

\[
\mathscr E_m'(z_E)
=
\langle m_h\,\partial_z e(z_E)\rangle.
\]

Let

\[
\bar m:=\langle m_h\rangle>0.
\]

Since

\[
\langle\partial_z e(z_E)\rangle
=
\mathscr E'(z_E)=0,
\]

we obtain

\[
\boxed{
Z_m(z_E)
=
-\langle m_h\partial_z e(z_E)\rangle
=
-\operatorname{Cov}_\mu\!\left(m_h,\partial_z e(z_E)\right).
}
\]

Equivalently, for the normalized production-conditioned expectation

\[
\mathbb E_m[f]
:=
\frac{\langle m_h f\rangle}{\bar m},
\]

\[
\boxed{
\frac{Z_m(z_E)}{\bar m}
=
-\mathbb E_m[\partial_z e(z_E)].
}
\]

Thus positive `Z_m(z_E)` means that production-marked recurrent states preferentially lie on the decreasing side of the depth-energy profile at the depth where the unconditional mean has zero slope.

## 3. This is a phase-selection statement, not monotonicity

The identity does not imply that every state satisfies

\[
\partial_z e(z_E)<0.
\]

Nor does it imply

\[
\mathscr E_m'(z)<0
\]

for all depths.

It states only that the production marker is statistically anticorrelated with the instantaneous depth slope at `z_E`.

Hence

\[
\boxed{
Z_m(z_E)>0
\Longleftrightarrow
\text{production-conditioned depth-phase bias at }z_E.
}
\]

This is genuinely signed information, but it is correlation information rather than a one-way state variable.

## 4. Explicit endpoint-compatible anti-model

The endpoint data of M19-298 alone cannot force the sign of `Z_m(z_E)`.

Take a compact probability space with a bounded mean-zero observable `a(Y)` and choose a nonnegative smooth base profile `E_0(z)` satisfying

\[
E_0(\infty)=0,
\qquad
E_0'(z_E)=0.
\]

Let `phi(z)` be smooth, decaying at infinity, and satisfy

\[
\phi'(z_E)<0.
\]

For sufficiently small `epsilon`, define

\[
e(z,Y)=E_0(z)+\epsilon a(Y)\phi(z)\ge0.
\]

Choose a nonnegative event marker `m(Y)` positively correlated with `a(Y)`. Then

\[
\langle\partial_z e(z_E)\rangle=0,
\]

while

\[
-\langle m\partial_z e(z_E)\rangle
=
-\epsilon\phi'(z_E)\langle ma\rangle
>0.
\]

The profile can retain the same finite terminal value and zero large-z endpoint.

Therefore

\[
\boxed{
\mathscr E'(z_E)=0,
\quad
\mathscr E_m(\infty)=0,
\quad
\mathscr E_m(0)<\infty
\not\Rightarrow
Z_m(z_E)=0
}
\]

and do not contradict `Z_m(z_E)>0`.

This anti-model is only a logical firewall; it is not asserted to solve Navier--Stokes.

## 5. Quantitative covariance bound

Cauchy--Schwarz gives

\[
\boxed{
|Z_m(z_E)|
\le
\sqrt{\operatorname{Var}(m_h)}
\sqrt{\left\langle|\partial_z e(z_E)|^2\right\rangle}.
}
\]

Since the retained fixed-depth hull is smooth and compact, the right-hand side is finite.

Thus the depth channel has a finite local capacity. A contradiction would require a certified lower bound on `Z_m(z_E)` exceeding this capacity, or a stronger PDE relation forcing the covariance to vanish or have the opposite sign. No such inequality is currently established.

## 6. Relation to M19-298

M19-298 gives the global signed-depth budget

\[
\int_0^\infty Z_m(z)dz
=
\mathscr E_m(0).
\]

M19-299 shows why a positive value at one selected depth does not by itself consume that budget monotonically: `Z_m` may change sign in depth and the selected sign is a correlation with the production phase.

Therefore the next valid calculation must use the full conditioned wedge PDE, not endpoint data alone.

## 7. Next target

Define conditioned wedge observables

\[
\mathscr J_m(z):=\langle m_hj(z)\rangle,
\qquad
\mathscr D_m(z):=\langle m_hd(z)\rangle,
\]

and event-boundary current

\[
\mathscr B_m(z)
:=-\langle(\mathcal L_qm_h)j(z)\rangle.
\]

Derive the exact full-depth conditioned ODE and classify every sign change of `Z_m` as current redistribution, dissipation, or event-boundary hysteresis.

---

\[
\boxed{\text{M19-299 COMPLETE; Z_cond IS A PRODUCTION--DEPTH-SLOPE COVARIANCE, NOT AN ENDPOINT-FORCED MONOTONE DRIFT.}}
\]