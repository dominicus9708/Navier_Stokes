# DSD M17-370 — Partition-free dual-weight flux inequality cancels amplitude and forces `Phi_r \lesssim r^{5/2}(M_r H_r)^{1/2}`

Date: 2026-09-08  
Canonical ID: **M17-370**

Status: **ACTIVE PARTITION-FREE CRITICAL FLUX INEQUALITY**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Scale-`r` negative-coefficient line family

Work at one fixed physical or record-normalized snapshot on a regular CE-H region.

Let

\[
q:=\kappa_-\ge0.
\]

Consider a measurable positively oriented material-flux family `F_r` such that on the retained line portion

\[
\boxed{
q\ge c_q r^{-2}
}
\]

and every participating flux label has retained arclength at least

\[
\boxed{
\ell_\lambda\ge c_\ell r.
}
\]

Let its total directed flux be

\[
\boxed{
\Phi_r:=\int_{F_r}d\Phi.
}
\]

No decomposition into finitely many tubes is chosen.

## 2. Exact flux-coordinate forms

For regular vortex-line flux coordinates,

\[
\boxed{
dy=\frac{ds\,d\Phi}{\rho},
\qquad \rho=|W|.
}
\]

The negative critical coefficient mass on the family is

\[
\boxed{
M_r
:=
\int_{F_r}q^{3/2}dy
=
\int_{F_r}q^{3/2}\rho^{-1}ds\,d\Phi.
}
\]

The raw `H2` charge carried by the same family satisfies

\[
\boxed{
H_r
:=
\int_{F_r}|\Delta W|^2dy
=
\int_{F_r}q^2\rho\,ds\,d\Phi,
}
\]

because on the negative CE-H phase

\[
\Delta W=\kappa W=-qW.
\]

The reciprocal amplitude weights `rho^{-1}` and `rho` are the key point.

## 3. Amplitude cancellation by Cauchy--Schwarz

Define

\[
J_r
:=
\int_{F_r}q^{7/4}ds\,d\Phi.
\]

Since

\[
q^{7/4}
=
\left(q^{3/2}\rho^{-1}\right)^{1/2}
\left(q^2\rho\right)^{1/2},
\]

Cauchy--Schwarz in the measure `ds dPhi` gives

\[
\boxed{
J_r^2\le M_rH_r.
}
\]

This estimate is exact and does not use a packet decomposition, amplitude floor, or tube-count parameter.

## 4. Lower bound from coefficient scale and retained length

On `F_r`,

\[
q^{7/4}
\ge
c_q^{7/4}r^{-7/2}.
\]

Each flux label contributes length at least `c_l r`, hence

\[
\begin{aligned}
J_r
&\ge
c r^{-7/2}
\int_{F_r}\ell_\lambda d\Phi\\
&\ge
c r^{-7/2}(c_\ell r)\Phi_r.
\end{aligned}
\]

Therefore

\[
\boxed{
J_r\ge c\Phi_r r^{-5/2}.
}
\]

Combining with Section 3,

\[
\boxed{
\Phi_r^2r^{-5}
\lesssim
M_rH_r.
}
\]

Equivalently,

\[
\boxed{
\Phi_r
\lesssim
r^{5/2}(M_rH_r)^{1/2}.
}
\]

This is the main partition-free inequality.

## 5. Companion enstrophy inequality

Let

\[
E_r:=\int_{F_r}|W|^2dy
=\int_{F_r}\rho\,ds\,d\Phi.
\]

Now

\[
q^{3/4}
=
\left(q^{3/2}\rho^{-1}\right)^{1/2}
\rho^{1/2}.
\]

Thus

\[
\left(
\int_{F_r}q^{3/4}ds\,d\Phi
\right)^2
\le M_rE_r.
\]

The scale and length lower bounds give

\[
\int_{F_r}q^{3/4}ds\,d\Phi
\ge c\Phi_r r^{-1/2}.
\]

Hence

\[
\boxed{
\Phi_r
\lesssim
r^{1/2}(M_rE_r)^{1/2}.
}
\]

This recovers the `r^{1/2}` flux thinning seen in M17-368, but now for the **entire flux family without any fragmentation dependence**.

## 6. Scale audit

Under the Navier--Stokes parabolic scaling,

\[
q_R=R^2q,
\qquad
M_R=M,
\]

\[
H_R=R^5H,
\qquad
E_R=RE,
\]

and intrinsic length scales transform as

\[
r_R=r/R.
\]

Therefore

\[
r_R^{5/2}H_R^{1/2}=r^{5/2}H^{1/2},
\]

and

\[
r_R^{1/2}E_R^{1/2}=r^{1/2}E^{1/2}.
\]

The total vorticity flux is scale invariant. Both inequalities are therefore dimensionally and parabolically consistent.

## 7. Consequence on a compact local-H2 branch

If on the relevant fixed normalized region

\[
M_r\le M_*<\infty
\]

and

\[
H_r\le H_*<\infty,
\]

then

\[
\boxed{
\Phi_r\le C(M_*H_*)^{1/2}r^{5/2}.
}
\]

Thus a strict subscale sequence `r_j -> 0` cannot carry a fixed positive amount of negative-line material flux while both the critical coefficient mass and local raw-`H2` charge remain uniformly bounded.

Any fixed-flux strict-subscale survivor must therefore leave at least one compact condition through

\[
\boxed{
G_{M_{3/2}\ decompactification}
\lor
G_{raw\text{-}H2\ decompactification}
\lor
G_{retained\ length/geometry\ failure}.
}
\]

## 8. Why this improves M17-369

M17-369 obtained a multiplicity floor for one selected packet partition. The present result removes the partition entirely.

Flux fragmentation cannot evade

\[
\Phi_r^2r^{-5}\lesssim M_rH_r,
\]

because both sides are defined on the full measurable flux family.

This realizes the useful DSD heuristic from M17-369: once a bookkeeping quantity is partition-sensitive, search for a representation-invariant descriptor before using it in the proof tree.

## 9. Remaining limitation

The inequality does **not** prove that `Phi_r` has a positive lower bound on the moving nodal coefficient population.

If

\[
\Phi_r=O(r^{5/2})
\]

or smaller, a critical coefficient population can remain almost fluxless and the estimate is consistent.

Therefore the next target is to quantify what such flux thinning forces on the amplitude distribution of the same nodal family, and whether that distribution is compatible with compact CE-H material genealogy.

## 10. Audit verdict

**PASS.**

The central result is

\[
\boxed{
\Phi_r
\lesssim
r^{5/2}(M_rH_r)^{1/2},
}
\]

with no tube-count or fragmentation assumption.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]