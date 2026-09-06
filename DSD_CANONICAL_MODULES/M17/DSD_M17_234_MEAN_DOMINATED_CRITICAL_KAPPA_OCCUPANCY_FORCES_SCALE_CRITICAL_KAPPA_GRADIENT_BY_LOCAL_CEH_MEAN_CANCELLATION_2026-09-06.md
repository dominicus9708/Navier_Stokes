# DSD M17-234 — Mean-dominated critical kappa occupancy forces a scale-critical kappa gradient by local CE-H mean cancellation

Date: 2026-09-06  
Canonical ID: **M17-234**

Status: **COEFFICIENT-CONSTANCY PRUNING / M17-233 SHOWS THAT A MEAN-DOMINATED ROOT INTRINSIC CE-H PACKET WITH NO DIMENSIONLESS KAPPA SPIKE HAS AN AMPLITUDE-INDEPENDENT CRITICAL POTENTIAL MASS `int |kappa|^(3/2)>=c>0`. A NEAR-CONSTANT POTENTIAL CANNOT CARRY THIS BRANCH WHILE `W` REMAINS CLOSE TO A NONZERO SPATIAL MEAN. PROJECT `Delta W=kappa W` ONTO THE MEAN DIRECTION AND TEST AGAINST A COMPACT BUFFER CUTOFF. THE CONSTANT PART OF `W` DROPS OUT OF `int W Delta phi`, SO THE SIGNED WEIGHTED MEAN OF `kappa` IS `O(sqrt(theta) ell^-2)`. FOR THE SAME SMALL MEAN-DOMINATION THRESHOLD, THIS IS TOO SMALL TO EXPLAIN THE FIXED `L^(3/2)` NORM OF `kappa`. A WEIGHTED POINCARE INEQUALITY THEREFORE FORCES `ell ||grad kappa||_(L^(3/2)) >= c>0`. THUS THE BOUNDED-DIMENSIONLESS-KAPPA COEFFICIENT RETURN IS ACTUALLY A SCALE-CRITICAL KAPPA-GRADIENT CHANNEL. THE SURVIVOR IS PALINSTROPHY, DIMENSIONLESS KAPPA SPIKE, KAPPA-GRADIENT CRITICALITY, OR NODAL/INTERFACE FAILURE. GLOBAL REGULARITY REMAINS UNPROVED.**

---

## 1. Input from M17-233

Let `B=B_r(q)` be a root intrinsic buffer with

\[
r=A\ell
\]

and inner core `K subset B`.

Write

\[
W=c+w,
\qquad
c:=\frac1{|B|}\int_BWdy,
\qquad
\int_Bwdy=0.
\]

Assume the mean-dominated branch

\[
\boxed{
V:=\int_B|w|^2dy
<\theta M,
\qquad
M:=\int_B|W|^2dy.
}
\]

Then

\[
|B||c|^2=M-V>(1-\theta)M.
\]

Assume also the bounded dimensionless coefficient branch of M17-233,

\[
\boxed{
\|\kappa\|_{L^\infty(B)}
\le K_0\ell^{-2}.
}
\]

M17-233 gives, after choosing `theta` sufficiently small depending on `K0` and geometry,

\[
\boxed{
\int_K|\kappa|^{3/2}dy
\ge d_0>0,
}
\]

where `d0` is independent of `ell` and of the packet amplitude.

---

## 2. Project CE-H onto the local mean direction

Because the packet is mean dominated, `c` is nonzero for sufficiently small `theta`.

Set

\[
\boxed{e:=\frac{c}{|c|}}
\]

and define the scalar component

\[
u:=e\cdot W
=|c|+v,
\qquad
v:=e\cdot w.
\]

The CE-H elliptic equation

\[
\Delta W=\kappa W
\]

implies

\[
\boxed{
\Delta u=\kappa u.
}
\]

Also

\[
\|v\|_{L^2(B)}\le V^{1/2}.
\]

---

## 3. Compact cutoff identity

Choose a fixed-shape smooth cutoff `phi` such that

\[
0\le\phi\le1,
\qquad
\phi\equiv1\text{ on }K,
\qquad
\operatorname{supp}\phi\subset B.
\]

Its scaling satisfies

\[
\boxed{
\|\Delta\phi\|_2\le C_A r^{-1/2},
\qquad
\|\phi\|_2\le C_A r^{3/2},
\qquad
\int_B\phi\,dy\asymp_A r^3.
}
\]

Multiply

\[
\Delta u=\kappa u
\]

by `phi` and integrate over `R^3`.

Since `phi` is compactly supported,

\[
\int\phi\Delta u
=\int u\Delta\phi.
\]

Also the constant mean satisfies

\[
\int |c|\Delta\phi=0.
\]

Therefore

\[
\boxed{
|c|\int\phi\kappa
=
\int v\Delta\phi
-
\int\phi\kappa v.
}
\]

This is the local CE-H mean-cancellation identity.

---

## 4. The signed kappa mean is small

By Cauchy--Schwarz,

\[
\left|\int v\Delta\phi\right|
\le
V^{1/2}\|\Delta\phi\|_2.
\]

Also

\[
\left|\int\phi\kappa v\right|
\le
\|\kappa\|_\infty
V^{1/2}\|\phi\|_2.
\]

From

\[
|c|^2
>\frac{(1-\theta)M}{|B|}
\]

and

\[
V<\theta M,
\]

we get

\[
\frac{V^{1/2}}{|c|}
\le
C\sqrt{\frac{\theta}{1-\theta}}\,|B|^{1/2}
\le C_A\sqrt\theta\,r^{3/2}.
\]

Hence

\[
\begin{aligned}
\left|\int\phi\kappa\right|
&\le
C_A\sqrt\theta\,r^{3/2}r^{-1/2}
+
C_A\sqrt\theta\,r^{3/2}
K_0\ell^{-2}r^{3/2}\\
&\le
C_{A,K_0}\sqrt\theta\,\ell,
\end{aligned}
\]

because `r=A ell`.

Define the weighted local mean

\[
\boxed{
\kappa_\phi
:=
\frac{\int\phi\kappa}{\int\phi}.
}
\]

Since

\[
\int\phi\asymp_A\ell^3,
\]

we obtain

\[
\boxed{
\ell^2|\kappa_\phi|
\le C_{A,K_0}\sqrt\theta.
}
\]

Thus the signed potential mean becomes arbitrarily small in intrinsic units when the vorticity packet becomes strongly mean dominated.

---

## 5. The absolute critical kappa mass cannot be explained by the small mean

M17-233 gives

\[
\|\kappa\|_{L^{3/2}(K)}
\ge d_0^{2/3}.
\]

The constant `kappa_phi` restricted to `K` satisfies

\[
\|\kappa_\phi\|_{L^{3/2}(K)}
=|\kappa_\phi||K|^{2/3}.
\]

Since

\[
|K|\asymp_A\ell^3,
\]

Section 4 gives

\[
\boxed{
\|\kappa_\phi\|_{L^{3/2}(K)}
\le C_{A,K_0}\sqrt\theta.
}
\]

Choose `theta` smaller if necessary so that

\[
C_{A,K_0}\sqrt\theta
\le\frac12d_0^{2/3}.
\]

Then the triangle inequality yields

\[
\boxed{
\|\kappa-\kappa_\phi\|_{L^{3/2}(K)}
\ge\frac12d_0^{2/3}.
}
\]

Thus the critical potential mass is genuinely oscillatory/nonconstant; it cannot be supplied by a nearly constant local eigenvalue.

---

## 6. Weighted Poincare forces a critical kappa gradient

For the fixed-shape pair `K subset B` and the weighted mean `kappa_phi`, the standard local Poincare inequality gives

\[
\boxed{
\|\kappa-\kappa_\phi\|_{L^{3/2}(K)}
\le C_A r\|\nabla\kappa\|_{L^{3/2}(B)}.
}
\]

Combining with Section 5,

\[
\boxed{
r\|\nabla\kappa\|_{L^{3/2}(B)}
\ge c_{A,K_0}>0.
}
\]

Since `r=A ell`, equivalently

\[
\boxed{
\ell\|\nabla\kappa\|_{L^{3/2}(B)}
\ge c'_{A,K_0}>0.
}
\]

This quantity is scale invariant in three dimensions for a coefficient with scaling `kappa~length^-2`.

Indeed `grad kappa~length^-3`, and under `y=q+ell z`,

\[
\ell\|\nabla\kappa\|_{L^{3/2}(B_{A\ell})}
=
\|\nabla_z(\ell^2\kappa(q+\ell z))\|_{L^{3/2}(B_A)}.
\]

---

## 7. Updated coefficient gate

M17-233--234 therefore give the root intrinsic implication

\[
\boxed{
G_{intrinsic\ H2/L2\ spectral}
\Longrightarrow
H_{intrinsic\ palinstrophy}
\lor
G_{dimensionless\ \kappa\ spike}
\lor
H_{critical\ \nabla\kappa\ occupancy}
\lor
G_{nodal/interface}.
}
\]

The former static branch

\[
H_{critical\ \kappa\ L^{3/2}\ occupancy}
\]

is sharpened to a nonconstant coefficient-gradient branch whenever the dimensionless coefficient ceiling holds.

---

## 8. Relation to M17-145 and M5-687

M17-145 derives a genuine weighted diffusion/damping law for directional `kappa` gradients, while M5-687 gives a division-free polynomial

\[
\mathcal P_\kappa=\rho^4\nabla\kappa
\]

and a positive `rho^2|grad kappa|^2` diffusion charge on the compact high-amplitude CE-H hull.

M17-234 differs in two respects:

1. its lower bound is **unweighted and amplitude independent**;
2. it is localized at the remote intrinsic packet scale.

Therefore it is not automatically controlled by the existing `rho^2`-weighted diffusion ledger, especially on the low-amplitude remote branch.

The next task is to determine whether mean domination is strong enough to transfer a fixed portion of this unweighted gradient charge to a region with a usable amplitude floor, or whether the gradient can still concentrate inside the small cancellation set.

---

## 9. DSD audit

- The CE-H test is performed on the original `W`, not on a mean-subtracted descendant.
- The constant part disappears only after integration against the compact Laplacian test; no boundary condition on `W` is assumed.
- The signed mean and absolute `L3/2` norm of `kappa` are kept distinct.
- Poincare is applied to `kappa` only on the regular coefficient branch; nodal/interface loss is exported.
- The result produces an amplitude-independent coefficient-gradient charge, not yet a finite Navier--Stokes energy charge.
- Existing `rho^2`-weighted diffusion estimates cannot be imported without an amplitude-transfer argument.
- Global regularity remains unproved.

---

\[
\boxed{\text{GLOBAL REGULARITY REMAINS UNPROVED.}}
\]
