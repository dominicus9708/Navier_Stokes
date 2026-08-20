# Sharp Vorticity-Radius Upper Bound for the P_V H1 Threshold — 2026-08-20

Overall status: **NEW EXPLICIT SCALE-RADIUS BARRIER — GLOBAL REGULARITY NOT PROVED.**

This note derives an explicit universal bound on the remaining H1 threshold quotient

\[
\eta_{VI}(S)
=\frac{-\langle\mathcal R_{VI},-\Delta S\rangle}{\|\Delta S\|_2^2}
=\frac{N(S)}{H(S)}.
\]

The result is

\[
\boxed{
\eta_{VI}(S)
\le
C_0\,\|\omega\|_\infty R_\omega^2,
\qquad
C_0=\frac{8\sqrt2\,5^{3/4}}{27\sqrt\pi}
\approx0.79048528,
}
\]

where

\[
R_\omega^2
=\frac{\int |x-X|^2|\omega|^2dx}{\|\omega\|_2^2}
\]

is the vorticity rms radius about any chosen center `X`.

Thus in first-hitting variables with `||Omega||_infty=1`, a viscosity-threshold event `eta_VI>=nu` requires

\[
\boxed{
R_\Omega^2\ge\frac{\nu}{C_0},
\qquad
R_\Omega\ge C_0^{-1/2}\sqrt\nu
\approx1.1248\sqrt\nu.
}
\]

For the standard normalization `nu=1`, every threshold core with rms vorticity radius below approximately `1.125` is rigorously subcritical.

---

## 1. Sharp pointwise H1 production bound

The earlier trace-free range calculation gives

\[
N(S)
\le
\frac4{\sqrt6}
\int |S||\nabla S|^2dx.
\]

Set

\[
P=\|\nabla S\|_2^2,
\qquad
H=\|\Delta S\|_2^2.
\]

Using Hölder,

\[
\int|S||\nabla S|^2
\le
\|S\|_6\,\|\nabla S\|_{12/5}^2.
\]

The sharp Sobolev inequality in `R^3` is

\[
\|f\|_6\le C_S\|\nabla f\|_2,
\qquad
C_S=\frac{2^{2/3}}{\sqrt3\,\pi^{2/3}}.
\]

Applied componentwise through `|S|` and `|grad S|`, together with interpolation

\[
\|\nabla S\|_{12/5}
\le
\|\nabla S\|_2^{3/4}\|\nabla S\|_6^{1/4}
\]

and

\[
\|\nabla S\|_6
\le C_S\|\nabla^2S\|_2
=C_S\|\Delta S\|_2,
\]

we obtain

\[
\boxed{
N(S)
\le
C_N P^{5/4}H^{1/4},
}
\]

with

\[
C_N
=\frac4{\sqrt6}C_S^{3/2}
=\frac{4\sqrt2\,3^{3/4}}{9\pi}.
\]

Hence

\[
\eta_{VI}\le C_NP^{5/4}H^{-3/4}.
\]

---

## 2. Exact strain-vorticity L2 identities

For a divergence-free velocity field,

\[
\boxed{
\|S\|_2^2=\frac12\|\omega\|_2^2,
}
\]

and, because derivatives commute with the Fourier strain-vorticity relation,

\[
\boxed{
\|\nabla S\|_2^2
=\frac12\|\nabla\omega\|_2^2,
\qquad
\|\Delta S\|_2^2
=\frac12\|\Delta\omega\|_2^2.
}
\]

Write

\[
Z=\|\omega\|_2^2,
\qquad
M_\omega=\int|x-X|^2|\omega|^2dx.
\]

Then `E=||S||_2^2=Z/2`.

---

## 3. Eliminate P using interpolation

Cauchy-Schwarz in Fourier space gives

\[
P^2\le EH.
\]

Therefore

\[
\eta_{VI}
\le
C_NE^{5/8}H^{-1/8}.
\]

---

## 4. Heisenberg lower bound on H

The three-dimensional Heisenberg inequality applied to the vorticity vector field gives

\[
M_\omega\|\nabla\omega\|_2^2
\ge
\frac94 Z^2.
\]

Also

\[
\|\nabla\omega\|_2^4
\le
Z\|\Delta\omega\|_2^2.
\]

Since `H=||Delta omega||_2^2/2`,

\[
\boxed{
H
\ge
\frac{81}{32}\frac{Z^3}{M_\omega^2}.
}
\]

Substituting into the previous estimate yields the exact cancellation of all powers of two:

\[
\boxed{
\eta_{VI}
\le
\frac{C_N}{\sqrt3}(Z M_\omega)^{1/4}.
}
\]

---

## 5. Bathtub lower bound on vorticity moment

Let

\[
A=\|\omega\|_\infty.
\]

Among all densities

\[
0\le f=|\omega|^2\le A^2
\]

with fixed mass

\[
\int f=Z,
\]

the second moment about a center is minimized by filling a ball at the maximal density `A^2`.

The resulting sharp moment lower bound is

\[
\boxed{
M_\omega
\ge
C_B A^{-4/3}Z^{5/3},
}
\]

where

\[
C_B
=\frac{3^{5/3}}{5(4\pi)^{2/3}}
=\frac{3\,6^{2/3}}{20\pi^{2/3}}.
\]

Define

\[
R_\omega^2=M_\omega/Z.
\]

Then the bathtub inequality is equivalent to

\[
Z
\le
C_B^{-3/2}A^2R_\omega^3.
\]

Thus

\[
(ZM_\omega)^{1/4}
=Z^{1/2}R_\omega^{1/2}
\le
C_B^{-3/4}A R_\omega^2.
\]

---

## 6. Explicit constant

Combining the previous steps,

\[
\eta_{VI}
\le
\frac{C_N}{\sqrt3}C_B^{-3/4}
A R_\omega^2.
\]

The constant simplifies to

\[
\boxed{
C_0
=\frac{8\sqrt2\,5^{3/4}}{27\sqrt\pi}
\approx0.79048528.
}
\]

Hence

\[
\boxed{
\eta_{VI}
\le
0.79049\,\|\omega\|_\infty R_\omega^2.
}
\]

---

## 7. First-hitting consequence

In normalized first-hitting variables,

\[
\|\Omega\|_\infty=1.
\]

Therefore

\[
\boxed{
\eta_{VI}
\le
C_0R_\Omega^2.
}
\]

For H1 production to meet the viscous threshold,

\[
\eta_{VI}\ge\nu,
\]

it is necessary that

\[
\boxed{
R_\Omega^2\ge\frac{\nu}{C_0}
\approx1.26505\,\nu,
}
\]

or

\[
\boxed{
R_\Omega\ge1.1248\sqrt\nu.
}
\]

Thus the dangerous projective H1 core cannot be arbitrarily concentrated. It must occupy at least a viscous-scale rms radius.

---

## 8. Interpretation for the proof tree

This creates a new quantitative split:

\[
\boxed{
R_\Omega<1.1248\sqrt\nu
\Longrightarrow
\eta_{VI}<\nu
\Longrightarrow
\text{no recurrent P_V H1 threshold}.
}
\]

The only remaining smooth threshold core must be **broad enough** in normalized vorticity rms radius. If that radius escapes to infinity, it is spatial non-tightness/turnover `T`; if it remains bounded, the remaining variational class is confined to the compact annulus

\[
1.1248\sqrt\nu\lesssim R_\Omega\le R_*.
\]

The next target is to combine this lower viscous-radius barrier with the first-hitting analyticity radius and the bounded-core/remote-halo separation, seeking either a strict upper radius for an active non-`T` core or a stronger shape factor reducing the constant `C_0` on the strain-compatible first-hitting class.

Status: **THE P_V VISCOSITY THRESHOLD REQUIRES A MINIMUM VORTICITY RMS RADIUS. WITH NU=1, ALL FIRST-HITTING CORES BELOW R_OMEGA APPROX 1.125 ARE RIGOROUSLY SUBCRITICAL. GLOBAL REGULARITY REMAINS UNPROVED.**