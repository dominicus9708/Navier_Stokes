# M19-189 — Nonzero rotation-orbit dimension and time-tangent independence raise the universal aperiodic payment from three to five hard channels

**Date:** 2026-09-13  
**Status:** ACTIVE CALCULATION / STRICT SYMMETRY-COUNT IMPROVEMENT

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Previous universal count

M19-185 used only the always-present time tangent and obtained

\[
N\ge2\quad\Longrightarrow\quad M\ge3,
\]

where `N` is the symmetry-quotient hard dimension and `M` is the number of observable neutral hard channels available to the collective trace estimate.

This undercounted the exact rotation orbit.

## 2. A nonzero decaying divergence-free state cannot be SO(3)-invariant

Suppose a vector field `U` is invariant under every spatial rotation:

\[
U(Qy)=QU(y)
\qquad\forall Q\in SO(3).
\]

Then equivariance forces

\[
U(y)=f(|y|)y.
\]

Divergence-free gives

\[
0=\nabla\cdot U
=3f(r)+rf'(r),
\]

hence

\[
f(r)=cr^{-3}.
\]

Regularity at the origin and the retained smooth whole-space corridor force `c=0`.

Therefore

\[
\boxed{
U\neq0
\Longrightarrow
\operatorname{Stab}_{SO(3)}(U)\neq SO(3).
}
\]

The connected stabilizer of a nonzero state has dimension at most one. Hence

\[
\boxed{
\dim(SO(3)\cdot U)\ge2.
}
\]

Thus there are at least two linearly independent nonzero rotation tangents

\[
\mathcal R_{J_1}U,
\qquad
\mathcal R_{J_2}U.
\]

Each solves the exact linearized equation.

## 3. Their vorticities are genuine observation channels

If

\[
\nabla\times(\mathcal R_JU)=0,
\]

then `R_J U` is both divergence-free and curl-free. Under the retained decay/whole-space class it is zero. Thus `J` lies in the stabilizer direction.

Therefore independent rotation-orbit tangents produce independent nonzero linearized-vorticity observation channels.

## 4. The time tangent is independent of rotation tangents off the RSS branch

The autonomous equation gives the exact linearized solution

\[
W_t=\partial_sU.
\]

Assume at one time `s_0` that

\[
\partial_sU(s_0)
=\mathcal R_JU(s_0)
\]

for some fixed Lie-algebra element `J`.

Both sides solve the same homogeneous linearized equation. Their difference vanishes at `s_0`, so linearized uniqueness gives

\[
\partial_sU(s)=\mathcal R_JU(s)
\qquad\forall s.
\]

Thus `U` is a relative equilibrium / RSS orbit.

Consequently, on a genuinely non-RSS recurrent branch,

\[
\boxed{
\partial_sU
\notin
T_U(SO(3)\cdot U).
}
\]

The time tangent supplies one additional independent exact hard channel.

## 5. Universal aperiodic channel count

A genuinely aperiodic orbit in the rotation/time quotient requires

\[
N\ge2.
\]

Before quotienting, a non-RSS nonzero state therefore carries at least

\[
\underbrace{2}_{\text{extra quotient directions}}
+
\underbrace{2}_{\text{rotation orbit}}
+
\underbrace{1}_{\text{time tangent}}
=5
\]

independent observable hard channels.

Hence

\[
\boxed{
\text{genuinely aperiodic recurrent hard dynamics}
\Longrightarrow
M\ge5.
}
\]

On the generic stratum with discrete rotational isotropy,

\[
\dim(SO(3)\cdot U)=3,
\]

so in fact

\[
\boxed{M\ge6.}
\]

The universal count remains `M=5` because axisymmetric states have a one-dimensional rotation stabilizer and a two-dimensional orbit.

## 6. Improved dimension test

The M19-181/182 collective trace inequality for total channel count `M` is

\[
\frac14+\nu x
\le
\mathfrak A M^{-2/5}x^{3/5}
+
\mathfrak B_aM^{d(a)-1}x^{q(a)}.
\]

Therefore the universal aperiodic-exclusion test improves from `M=3` to

\[
\boxed{
\sup_{x\ge0}
\left[
\mathfrak A5^{-2/5}x^{3/5}
+
\mathfrak B_a5^{d(a)-1}x^{q(a)}
-\nu x
\right]
<\frac14.
}
\]

For `a=2`,

\[
\boxed{
\Psi_5(x)
=
5^{-2/5}\mathfrak A x^{3/5}
+
5^{-1/6}\mathfrak B_2 x^{1/4}
-\nu x.
}
\]

This is strictly stronger than the M19-185 three-channel criterion.

## 7. Firewall

The rotation tangents are removed when classifying quotient dynamics, but they remain legitimate neutral solutions paying the collective vorticity damping budget.

\[
\boxed{
\text{quotienting a symmetry}
\neq
\text{removing its compensation cost from the unquotiented linearized family}.
}
\]

---

\[
\boxed{\text{M19-189: GENUINE APERIODICITY MUST PAY AT LEAST FIVE HARD CHANNELS.}}
\]
