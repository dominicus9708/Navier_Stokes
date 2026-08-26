# DSD W1 Scalar Gain-Profile Nonclosure Audit

Date: 2026-08-26

Status: **AN EXPLICIT POSITIVE-DEFECT SCALAR GAIN PROFILE SATISFYING ALL CURRENT ONE-DIMENSIONAL AMPLITUDE-STATE CONSTRAINTS IS CONSTRUCTED / THEREFORE THE SCALAR AMPLITUDE REDUCTION ALONE CANNOT CONTRADICT W1 / ANY FINAL CLOSURE MUST USE SPATIAL VECTOR GEOMETRY, PRESSURE POISSON COUPLING, OR VORTICITY STRUCTURE / GLOBAL REGULARITY UNPROVED.**

## 1. Current scalar constraints

The invariant amplitude reduction is encoded by

\[
\bar G(\lambda)
=\langle J_P(\lambda)-\nu D_\lambda\rangle_\mu,
\]

\[
\bar K(\lambda)
=2\int_\lambda^{A}\bar G(\mu)d\mu,
\]

and

\[
\bar C(\lambda)
=\bar K(\lambda)+2\lambda\bar G(\lambda).
\]

Necessary scalar constraints include

\[
\bar K(\lambda)\ge0,
\qquad
\bar C(\lambda)\ge0,
\]

\[
\bar K(A)=\bar C(A)=0,
\]

and a positive endpoint defect

\[
\bar K(0+)=\bar C(0+)>0.
\]

## 2. Explicit toy profile

Fix constants

\[
g>0,
\qquad A>0,
\]

and define

\[
\boxed{
\bar G_{toy}(\lambda)
=g\left(1-\frac\lambda A\right),
\qquad 0\le\lambda\le A.
}
\]

Then

\[
\begin{aligned}
\bar K_{toy}(\lambda)
&=2\int_\lambda^A
 g\left(1-\frac\mu A\right)d\mu\\
&=\boxed{\frac gA(A-\lambda)^2}.
\end{aligned}
\]

Hence

\[
\bar K_{toy}(\lambda)\ge0,
\qquad
\bar K_{toy}(A)=0.
\]

## 3. Reconstructed weak-L3 coefficient

Using

\[
\bar C=\bar K+2\lambda\bar G,
\]

one obtains

\[
\boxed{
\bar C_{toy}(\lambda)
=\frac gA(A^2-\lambda^2).
}
\]

Therefore

\[
\bar C_{toy}(\lambda)\ge0,
\qquad
\bar C_{toy}(A)=0,
\]

and

\[
\boxed{
\bar C_{toy}(0)=gA>0.
}
\]

The associated low-amplitude distribution is

\[
\bar N_{toy}(\lambda)
=\frac{\bar C_{toy}(\lambda)}{\lambda^3}
\sim gA\,\lambda^{-3}
\]

as `lambda downarrow0`, exactly the required weak-L3 critical slope.

## 4. Endpoint mass identity

The total net gain is

\[
2\int_0^A\bar G_{toy}(\lambda)d\lambda
=2g\frac A2
=gA.
\]

Thus

\[
\boxed{
2\int_0^A\bar G_{toy}d\lambda
=\bar C_{toy}(0)
=\bar K_{toy}(0).
}
\]

All current one-dimensional amplitude identities are satisfied.

## 5. Consequence

There is no contradiction in the scalar amplitude-state equations themselves.

Therefore a final W1 closure cannot be obtained solely from

- positivity of `K`;
- positivity of `C`;
- the endpoint defect mass;
- the strict interior gain band;
- or the cumulative-tail constraints on `G`.

The missing information must come from the fact that `G` is not an arbitrary scalar source: it must be realized by

\[
\boxed{
\bar G(\lambda)
=\left\langle
J_P(\lambda)-\nu D_\lambda
\right\rangle_\mu
}
\]

for a divergence-free three-dimensional Navier--Stokes velocity field whose pressure satisfies the Poisson equation and whose vorticity obeys the stretching dynamics.

## 6. Updated proof target

The true remaining realization problem is

\[
\boxed{
\text{Can a nontrivial scalar gain profile of the required type be realized by}
\quad
(\nabla\cdot U=0,\ -\Delta P=\partial_iU_j\partial_jU_i,\ \Omega=\nabla\times U)
\quad
\text{on a compact recurrent W1 class?}
}
\]

A negative answer would close W1. No such realization theorem is proved here.

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
