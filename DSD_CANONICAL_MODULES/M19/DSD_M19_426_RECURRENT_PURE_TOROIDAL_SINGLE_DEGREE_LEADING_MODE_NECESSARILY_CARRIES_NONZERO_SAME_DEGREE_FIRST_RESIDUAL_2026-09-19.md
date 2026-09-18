# M19-426 — A recurrent pure toroidal single-degree leading mode necessarily carries a nonzero same-degree toroidal first residual

Date: 2026-09-19  
Canonical ID: **M19-426**  
Status: **HIGHER-TOROIDAL SPECTRAL CLASSIFICATION / ON ONE FIXED SPHERICAL DEGREE l THE TOROIDAL SELF-NONLINEARITY HAS ZERO TOROIDAL PROJECTION / THE SAME-DEGREE FIRST-RESIDUAL TOROIDAL MODE IS EXACTLY THE COERCIVE LINEAR LOG-RADIAL OPERATOR -d_q^2+d_q+l(l+1) / ITS BOUNDED TWO-SIDED RECURRENT KERNEL IS TRIVIAL / PURE SINGLE-DEGREE TOROIDAL SURVIVOR CANNOT BE RESIDUAL-SILENT / GLOBAL REGULARITY UNPROVED**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Pure toroidal fixed-degree leading trace

Let the leading terminal trace be radial-free and supported in one toroidal spherical eigenspace of degree \(l\ge1\):

\[
\boxed{
A(q,\omega)
=
\omega\times\nabla_{S^2}\psi(q,\omega),
}
\]

with

\[
\boxed{
-\Delta_{S^2}\psi
=
\lambda_l\psi,
\qquad
\lambda_l=l(l+1).
}
\]

The coefficient \(\psi(q,\cdot)\) may move arbitrarily inside the finite-dimensional degree-l eigenspace as q varies.

The physical field is

\[
v(x)
=
r^{-1}A(q,\omega).
\]

Since \(A_r=0\), it is divergence free automatically.

## 2. Linear viscous part preserves the toroidal eigenspace

For any Cartesian component of

\[
r^{-1}A(q,\omega),
\]

the critical scalar Laplacian formula gives

\[
\Delta v
=
r^{-3}
\left(
A_{qq}-A_q+\Delta_{S^2}A
\right).
\]

The angular momentum operator

\[
\omega\times\nabla_{S^2}
\]

commutes with \(\Delta_{S^2}\), so

\[
\boxed{
\Delta_{S^2}A
=
-\lambda_l A.
}
\]

Therefore

\[
\boxed{
-\Delta v
=
r^{-3}
\left(
-A_{qq}+A_q+\lambda_lA
\right).
}
\]

The linear stationary residual remains in the same toroidal degree-l space.

## 3. Toroidal projection of the nonlinear self-interaction

For a radial-free field,

\[
(v\cdot\nabla)v
=
r^{-3}
(A\cdot\nabla_{S^2})A.
\]

The tangential divergence-free/toroidal part of the surface nonlinear acceleration is controlled by the two-dimensional surface-vorticity transport.

Let

\[
\zeta
:=
\operatorname{curl}_{S^2}A.
\]

For

\[
A
=
\omega\times\nabla_S\psi,
\]

one has, up to the fixed orientation convention,

\[
\zeta
=
-\Delta_S\psi
=
\lambda_l\psi.
\]

The toroidal projection of the nonlinear acceleration has surface curl proportional to

\[
\boxed{
J(\psi,\zeta),
}
\]

where \(J\) is the spherical Jacobian/Poisson bracket.

But

\[
\zeta=\lambda_l\psi,
\]

so

\[
\boxed{
J(\psi,\zeta)
=
\lambda_lJ(\psi,\psi)
=
0.
}
\]

Since \(S^2\) has no nonzero harmonic one-forms, a tangential divergence-free field with zero surface curl is zero.

Therefore

\[
\boxed{
\mathbb P_{tor}
\left[
(A\cdot\nabla_S)A
\right]
=
0.
}
\]

Thus a single spherical eigenspace has no toroidal self-recharge through its quadratic convection.

## 4. Pressure cannot contribute to the toroidal projection

The pressure contribution is an angular gradient plus radial component.

Hence

\[
\boxed{
\mathbb P_{tor}\nabla p=0.
}
\]

Therefore the toroidal projection of the first stationary residual is purely linear.

## 5. Exact same-degree first-residual law

Let

\[
C
=
\mathcal R_{stat}[A,P]
\]

be the first terminal-jet coefficient in the M5-572 convention.

Then on the pure toroidal degree-l branch,

\[
\boxed{
C_{tor,l}
=
\left(
-\partial_q^2
+
\partial_q
+
\lambda_l
\right)A.
}
\]

Equivalently at the scalar streamfunction level,

\[
\boxed{
c_l
=
\left(
-\partial_q^2
+
\partial_q
+
\lambda_l
\right)\psi.
}
\]

No nonlinear same-degree toroidal term is missing from this equation.

## 6. Bounded recurrent kernel is trivial

If the same-degree toroidal residual vanished,

\[
C_{tor,l}=0,
\]

then every coefficient in the degree-l eigenspace would satisfy

\[
-b''+b'+\lambda_lb=0.
\]

The characteristic equation is

\[
\mu^2-\mu-\lambda_l=0.
\]

Since

\[
1+4l(l+1)
=
(2l+1)^2,
\]

the two exponents are

\[
\boxed{
\mu_+=l+1,
\qquad
\mu_-=-l.
}
\]

Thus

\[
b(q)
=
c_+e^{(l+1)q}
+
c_-e^{-lq}.
\]

A two-sided bounded recurrent orbit permits neither nonzero exponential.

Therefore

\[
\boxed{
C_{tor,l}=0
\quad\Longrightarrow\quad
A_{tor,l}=0
}
\]

on the bounded recurrent terminal hull.

Hence every nonzero pure toroidal single-degree recurrent leading trace has a nonzero same-degree toroidal first residual.

## 7. Invariant coercive identity

The result has a quantitative invariant-mean form.

Pair the exact residual equation with \(A\) and average in q.

The derivative term satisfies

\[
\left\langle
\int A\cdot A_q
\right\rangle
=0,
\]

and

\[
\left\langle
\int A\cdot(-A_{qq})
\right\rangle
=
\left\langle
\|A_q\|_2^2
\right\rangle.
\]

Therefore

\[
\boxed{
\left\langle
\int_{S^2}
A\cdot C_{tor,l}
\right\rangle
=
\left\langle
\|A_q\|_2^2
+
\lambda_l\|A\|_2^2
\right\rangle.
}
\]

For every nonzero recurrent mode,

\[
\boxed{
\left\langle
A\cdot C_{tor,l}
\right\rangle
>0.
}
\]

In particular, for \(l\ge2\),

\[
\boxed{
\lambda_l\ge6.
}
\]

Thus the higher-toroidal single-degree branch has a stronger fixed angular coefficient than the \(l=1\) mode.

## 8. Relation to M19-419

M19-419 proves more for \(l=1\): a pure toroidal l=1 leading trace not only carries a nonzero same-degree toroidal residual; its nonlinear/pressure sector also necessarily leaks into componentwise \(l=3\).

M19-426 isolates the universal part valid for every l:

\[
\boxed{
\text{single toroidal eigenspace}
\Longrightarrow
\text{nonzero same-degree residual by linear coercivity}.
}
\]

Whether \(l\ge2\) also forces a specific higher poloidal/residual harmonic depends on the detailed quadratic Clebsch--Gordan structure and is not needed for the present conclusion.

## 9. This still remains critical

The physical first residual is

\[
r^{-3}C_{tor,l}.
\]

Therefore the stronger coefficient \(\lambda_l\) changes only a fixed numerical angular gap.

It does not improve the physical scale power.

The M19-414 critical-summability firewall remains:

\[
\boxed{
\text{fixed recurrent toroidal residual}
\not\Rightarrow
\text{nonsummable raw-H2 ancestry cost}.
}
\]

## 10. Consequence for the T>=2 frontier

A higher-toroidal survivor cannot remain inside one angular degree while keeping its first jet quiet.

Therefore a T>=2 state can avoid a same-degree residual payment only through genuine spectral compensation involving

- another toroidal degree;
- a radial/poloidal component;
- or both.

This produces the next exact target:

\[
\boxed{
\mathcal C_{tor}^{cross-degree}:
\text{classify the nonlinear cross-degree toroidal interaction needed to cancel }
(-\partial_q^2+\partial_q+\lambda_l)A_l.
}
\]

The self-interaction within one l cannot perform that cancellation.

\[
\boxed{\text{M19-426 COMPLETE; PURE SINGLE-DEGREE TOROIDAL RECURRENCE NECESSARILY PAYS A SAME-DEGREE FIRST-RESIDUAL CHARGE.}}
\]

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
