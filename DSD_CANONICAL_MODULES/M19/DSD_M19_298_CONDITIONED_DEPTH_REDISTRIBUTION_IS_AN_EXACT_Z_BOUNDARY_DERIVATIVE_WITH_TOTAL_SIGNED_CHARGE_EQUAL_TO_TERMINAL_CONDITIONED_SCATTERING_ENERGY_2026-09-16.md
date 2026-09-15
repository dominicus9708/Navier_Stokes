# M19-298 — Conditioned depth redistribution is an exact z-boundary derivative with total signed charge equal to terminal conditioned scattering energy

**Date:** 2026-09-16  
**Status:** ACTIVE DYNAMIC-CORE CALCULATION / CONDITIONED DEPTH BUDGET IDENTIFIED / GLOBAL REGULARITY UNPROVED

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Input from M19-297

Let

\[
\mathscr E_m(z):=\langle m_h e(z)\rangle,
\qquad
m_h(Y)=m_{pd}(\sigma_{-h}Y),
\]

where the smooth event marker satisfies

\[
0\le m_h\le 1.
\]

The depth channel in the global conditioned wedge identity is

\[
\boxed{
Z_m(z):=-\mathscr E_m'(z).
}
\]

At the M19-269 selected depth, `Z_cond = Z_m(z_E)`.

## 2. Large-z endpoint from backward Type-I decay

M5-475 gives on the retained marked ancient branch

\[
\|V(s)\|_\infty\lesssim(-s)^{-1/2}
\qquad(s\to-\infty).
\]

In wedge variables

\[
u=r^{-1}F,
\qquad
z=(-s)/r^2.
\]

For fixed `q=log r`,

\[
|F(z,q,\omega)|
=r|V(-zr^2)|
\lesssim
r(zr^2)^{-1/2}
=z^{-1/2}.
\]

Therefore the normalized spherical energy satisfies uniformly on the compact marked hull

\[
\boxed{
e(z,Y)=\frac12\int_{S^2}|F|^2d\omega=O(z^{-1}).
}
\]

Since `m_h` is bounded,

\[
\boxed{
\mathscr E_m(z)\to0
\qquad(z\to\infty).
}
\]

Thus the large-z endpoint used heuristically in M19-297 is now certified on this retained Type-I ancient branch.

## 3. Terminal endpoint

At `z=0`, the wedge trace is the scattering datum

\[
F(0,q,\omega)=A(q,\omega).
\]

Hence

\[
\boxed{
\mathscr E_m(0)
=
\frac12
\left\langle
m_h
\int_{S^2}|A|^2d\omega
\right\rangle
\ge0.
}
\]

This is finite because the terminal compact-tail class has bounded scattering amplitude.

## 4. Exact full-depth signed budget

For every finite `R`, the fundamental theorem gives

\[
\int_0^R Z_m(z)dz
=
\mathscr E_m(0)-\mathscr E_m(R).
\]

Letting `R\to\infty` and using Section 2,

\[
\boxed{
\int_0^\infty Z_m(z)dz
=
\mathscr E_m(0)
=
\frac12
\left\langle
m_h
\int_{S^2}|A|^2d\omega
\right\rangle.
}
\]

Thus the complete signed depth charge is finite and exactly determined by the terminal conditioned `L2(S2)` scattering energy.

## 5. Structural meaning

`Z_m` is not a q-time coboundary of the type excluded by M19-271. However it is an exact derivative in the independent wedge-depth variable:

\[
\boxed{
Z_m=-\partial_z\mathscr E_m.
}
\]

Therefore it cannot be interpreted as a newly created source-free signed quantity. Its total signed charge is a boundary budget already present at `z=0`.

This yields the permanent distinction

\[
\boxed{
\text{non-coboundary in recurrent }q\text{-time}
\neq
\text{non-boundary resource in wedge depth }z.
}
\]

## 6. What this does not prove

The identity does not imply

\[
Z_m(z)\ge0
\]

pointwise. The conditioned depth profile may decrease, flatten, or locally rise.

Nor does finite total signed depth charge by itself bound the positive variation

\[
\int (Z_m)_+dz
\]

without an additional one-sided or total-variation estimate.

Therefore a positive value at the selected depth `z_E` is not yet contradictory.

## 7. Updated target

The next question is no longer whether `Z_m` is a new infinite signed payer. It is not.

The live question is whether the production-conditioned depth profile has one of two stronger properties:

1. a one-sided/monotone law forcing `Z_m\ge0` with a quantitative finite terminal budget;
2. an oscillatory/replenishing branch, in which case the depth sign changes themselves must be represented by explicit wedge transport terms.

Equivalently, classify

\[
\boxed{
\mathscr E_m(z)
=
\langle m_h e(z)\rangle
}
\]

as monotone finite-budget or recurrent depth redistribution.

---

\[
\boxed{\text{M19-298 COMPLETE; THE CONDITIONED DEPTH CHANNEL IS A FINITE EXACT z-BOUNDARY BUDGET, NOT A NEW UNBOUNDED SIGNED RESOURCE.}}
\]