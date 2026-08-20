# Vorticity-Hessian P_V Frontier — 2026-08-20

Overall status: **ACTIVE DSD-ASSISTED 3D NAVIER--STOKES PROOF ATTEMPT — GLOBAL REGULARITY NOT PROVED.**

This note continues `FRONTIER_CONTACT_RADIUS_2026-08-20.md`. The main new step is an exact vorticity-gradient representation of the `P_V` H1 production and a sharper explicit vorticity rms-radius barrier.

---

## 1. Starting H1 production

Let

\[
N(S)=-\langle \mathcal R_{VI},-\Delta S\rangle,
\qquad
H(S)=\|\Delta S\|_2^2,
\qquad
\eta_{VI}=N/H.
\]

The exact strain H1 ledger is

\[
\frac12\frac d{dt}\|\nabla S\|_2^2+\nu\|\Delta S\|_2^2=N.
\]

For the vorticity, define

\[
Z=\|\omega\|_2^2,
\qquad
D=\|\Delta\omega\|_2^2.
\]

The strain-vorticity isometry gives

\[
Z=2\|S\|_2^2,
\qquad
D=2H.
\]

---

## 2. Exact vorticity-gradient representation

Differentiate the vorticity equation

\[
\partial_t\omega+u\cdot\nabla\omega=S\omega+\nu\Delta\omega.
\]

After contracting with `partial_k omega`, summing over `k`, integrating, and using symmetry to remove the antisymmetric part of `grad u`, one obtains

\[
\frac12\frac d{dt}\|\nabla\omega\|_2^2+\nu\|\Delta\omega\|_2^2
=A+B-C,
\]

where

\[
A=\int S_{ij}\,\partial_k\omega_i\,\partial_k\omega_j\,dx,
\]

\[
B=\int \partial_kS_{ij}\,\partial_k\omega_i\,\omega_j\,dx,
\]

\[
C=\int S_{k\ell}\,\partial_k\omega_i\,\partial_\ell\omega_i\,dx.
\]

The previously established compatibility identity

\[
\langle-\Delta S,\omega\otimes\omega\rangle=0
\]

implies

\[
2B
=\int \partial_kS_{ij}\,\partial_k(\omega_i\omega_j)\,dx
=-\int\Delta S_{ij}\omega_i\omega_j\,dx
=0.
\]

Since

\[
\|\nabla\omega\|_2^2=2\|\nabla S\|_2^2,
\qquad
\|\Delta\omega\|_2^2=2\|\Delta S\|_2^2,
\]

comparison with the strain H1 ledger gives the exact identity

\[
\boxed{
2N=A-C.
}
\]

Equivalently, if `G=grad omega` with `G_{ki}=partial_k omega_i`, then

\[
\boxed{
N
=\frac12\int S:\left(G^TG-GG^T\right)dx.
}
\]

Thus `P_V` H1 production is driven exactly by the non-normality of the vorticity-gradient matrix. If `G` is normal, `G^TG=GG^T`, its local contribution vanishes.

---

## 3. Second integration-by-parts form

Using `B=0`,

\[
A
=-\int S_{ij}\omega_i\Delta\omega_j\,dx.
\]

For `C`, integration by parts and

\[
\partial_kS_{k\ell}=\frac12\Delta u_\ell
=-\frac12(\nabla\times\omega)_\ell
\]

give

\[
\int (\partial_kS_{k\ell})\,\omega_i\partial_\ell\omega_i\,dx
=-\frac14\int(\nabla\times\omega)\cdot\nabla|\omega|^2dx
=0,
\]

and therefore

\[
C
=-\int S_{k\ell}\omega_i\partial_{k\ell}\omega_i\,dx.
\]

Hence

\[
\boxed{
2N
=\int S_{ab}
\left(
\omega_i\partial_{ab}\omega_i
-\omega_a\Delta\omega_b
\right)dx.
}
\]

---

## 4. Sharp local operator bound

Write

\[
H_{ab,i}=\partial_{ab}\omega_i.
\]

For fixed `S` and `omega`, the coefficient tensor contracting `H` is

\[
K_{ab,i}
=\omega_iS_{ab}-\delta_{ab}(S\omega)_i.
\]

Because `S` is symmetric and trace-free,

\[
|K|^2
=|\omega|^2|S|^2+3|S\omega|^2.
\]

For every symmetric trace-free `3x3` matrix,

\[
|S\omega|^2
\le\frac23|S|^2|\omega|^2.
\]

Therefore

\[
\boxed{
|K|\le\sqrt3\,|S|\,|\omega|.
}
\]

The constant `sqrt(3)` is sharp at the purely algebraic level: equality in the range bound occurs for an axisymmetric trace-free matrix with `omega` along the eigenvector of largest absolute eigenvalue.

Consequently, with `W=||omega||_infinity`,

\[
2N
\le
\sqrt3\,W\|S\|_2\|\nabla^2\omega\|_2.
\]

In `R^3`, Plancherel gives

\[
\|\nabla^2\omega\|_2=\|\Delta\omega\|_2=D^{1/2}.
\]

Using `||S||_2=(Z/2)^{1/2}`,

\[
\boxed{
N
\le
\sqrt{\frac38}\,W\sqrt{ZD}.
}
\]

Since `H=D/2`,

\[
\boxed{
\eta_{VI}
\le
\sqrt{\frac32}\,W\sqrt{\frac ZD}.
}
\]

---

## 5. Explicit second-order uncertainty step

Let

\[
M_\omega
=\int|x-X|^2|\omega|^2dx,
\qquad
R_\omega^2=M_\omega/Z.
\]

Set

\[
P_\omega=\|\nabla\omega\|_2^2.
\]

The 3D Heisenberg inequality gives

\[
M_\omega P_\omega
\ge\frac94Z^2.
\]

Also

\[
P_\omega^2
=\langle-\Delta\omega,\omega\rangle^2
\le ZD.
\]

Therefore

\[
D
\ge
\frac{81}{16}\frac{Z^3}{M_\omega^2},
\]

hence

\[
\sqrt{\frac ZD}
\le
\frac49\frac{M_\omega}{Z}
=\frac49R_\omega^2.
\]

Substitution yields the sharpened radius estimate

\[
\boxed{
\eta_{VI}
\le
C_1\,W R_\omega^2,
\qquad
C_1=\frac{2\sqrt6}{9}
\approx0.54433105.
}
\]

This improves the previous explicit constant

\[
C_0\approx0.79048528.
\]

---

## 6. Sharpened first-hitting radius barrier

At first-hitting normalization,

\[
\|\Omega\|_\infty=1.
\]

Therefore

\[
\eta_{VI}\ge\nu
\]

forces

\[
R_\Omega^2
\ge
\frac{\nu}{C_1}
=
\frac{3\sqrt6}{4}\nu.
\]

Equivalently,

\[
\boxed{
R_\Omega
\ge
\sqrt{\frac{3\sqrt6}{4}}\,\sqrt\nu
\approx1.35540301\sqrt\nu.
}
\]

For `nu=1`, every first-hitting `P_V` threshold core with

\[
R_\Omega<1.3554
\]

is rigorously subcritical for the present H1 threshold quotient.

---

## 7. Ancient similarity-scale consequence

If the restricted Type-I ancient limit obeys

\[
\|\Omega(\tau)\|_\infty\le C_I/|\tau|,
\]

then any recurrent ancient threshold time with

\[
\eta_{VI}(\tau)\ge\nu
\]

must satisfy

\[
\boxed{
R_\Omega(\tau)
\ge
\sqrt{\frac{3\sqrt6}{4C_I}}\,
\sqrt{\nu|\tau|}.
}
\]

Thus the previous similarity-scale annulus lower edge can be increased by the factor

\[
\sqrt{C_0/C_1}\approx1.205.
\]

---

## 8. Equality and next rigidity target

The new bound uses three possible losses:

1. the local tensor bound `|K| <= sqrt(3)|S||omega|`;
2. global Cauchy alignment between `S`, `omega`, and `nabla^2 omega`;
3. the combined Heisenberg/interpolation lower bound for `D`.

Exact simultaneous equality is not expected for a nonzero finite-energy whole-space field. In particular, equality in

\[
P_\omega^2\le ZD
\]

would require an `L2(R^3)` Laplacian eigenfunction, which does not exist for a nonzero free-space field. Therefore the displayed constant is a rigorous explicit bound but is not expected to be globally attained.

The next local target is to quantify a positive defect from these equality conditions on the precompact non-H/T first-hitting class. Such a defect would lower `C_1` further and raise the minimum similarity-scale radius of any threshold recurrence.

A second target is to combine the new non-normality identity

\[
N=\frac12\int S:(G^TG-GG^T)
\]

with the earlier max-mid/projective geometry. Near-normal `grad omega` is automatically subcritical; near-saturation forces a strongly non-normal, approximately rank-one shear-like vorticity-gradient geometry, which should be tested against compact recurrence and finite-energy localization.

---

Status: **GLOBAL REGULARITY IS NOT PROVED. THE LOCAL NON-H/T `P_V` SURVIVOR NOW OBEYS A SHARPER EXPLICIT VORTICITY-RADIUS BARRIER: `R_Omega >= 1.355403*sqrt(nu)` AT FIRST HITTING. THE H1 PRODUCTION HAS ALSO BEEN REWRITTEN EXACTLY AS A STRAIN-WEIGHTED NON-NORMALITY COMMUTATOR OF `grad omega`.**