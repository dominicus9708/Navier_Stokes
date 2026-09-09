# DSD M17-454 — A mesoscopically thick negative-kappa enstrophy core restores palinstrophy coercivity by a wide cutoff and is ancestrally forbidden if persistent

Date: 2026-09-09  
Canonical ID: **M17-454**

Status: **ACTIVE MESOSCOPIC COERCIVITY THEOREM / M17-428 BOUNDARY-FIREWALL REFINEMENT**

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]

## 1. Motivation

M17-428 showed that an own-scale negative coefficient cell

\[
\Delta\Omega=\kappa\Omega,
\qquad
\kappa\sim-1
\]

cannot by itself give a uniform local palinstrophy lower bound because cutoff-boundary terms can be of the same order.

M17-450--452 now show that the surviving positive-flux carrier is transversely mesoscopic, with baseline participation radius at least `R^(1/2)` own-scales.

The present module tests whether this larger transverse thickness can suppress the M17-428 cutoff error.

## 2. Thick negative-kappa sub-tube hypothesis

At one record-normalized time, suppose there is a coherent subregion `U_R` of the diffuse tube and a core `U_R^core` such that

\[
\boxed{
\kappa_R\le-\kappa_*<0
\quad\text{on }U_R,
}
\]

with `kappa_*` independent of `R`.

Assume the core is separated from the transverse boundary of `U_R` by own-scale distance

\[
\boxed{L_R\to\infty.}
\]

Assume also a fixed enstrophy mass floor

\[
\boxed{
\int_{U_R^{core}}|\Omega_R|^2dx
\ge e_*>0.
}
\]

The total record enstrophy remains uniformly bounded by M17-450:

\[
\|\Omega_R\|_2^2\le E_I.
\]

## 3. Wide cutoff

Choose a smooth cutoff `eta_R` such that

\[
\eta_R=1
\quad\text{on }U_R^{core},
\]

\[
\operatorname{supp}\eta_R\subset U_R,
\]

and

\[
\boxed{
|\nabla\eta_R|\le \frac{C}{L_R}.
}
\]

This is the key difference from the own-scale cutoff in M17-428.

## 4. Integration by parts

Exact CE-H gives

\[
\Delta\Omega_R=\kappa_R\Omega_R.
\]

Multiply by `eta_R^2 Omega_R` and integrate:

\[
\int\eta_R^2|\nabla\Omega_R|^2dx
=
\int(-\kappa_R)\eta_R^2|\Omega_R|^2dx
-2\int\eta_R\Omega_R(\nabla\eta_R\cdot\nabla\Omega_R)dx.
\]

Let

\[
P_\eta:=\int\eta_R^2|\nabla\Omega_R|^2dx.
\]

By Young,

\[
2\left|\int\eta_R\Omega_R(\nabla\eta_R\cdot\nabla\Omega_R)\right|
\le
\frac12P_\eta
+2\int|\nabla\eta_R|^2|\Omega_R|^2dx.
\]

Therefore

\[
\boxed{
P_\eta
\ge
\frac23
\int(-\kappa_R)\eta_R^2|\Omega_R|^2dx
-
\frac43
\int|\nabla\eta_R|^2|\Omega_R|^2dx.
}
\]

## 5. Mesoscopic boundary error vanishes

The first term obeys

\[
\int(-\kappa_R)\eta_R^2|\Omega_R|^2dx
\ge
\kappa_*e_*.
\]

The cutoff error satisfies

\[
\int|\nabla\eta_R|^2|\Omega_R|^2dx
\le
\frac{C}{L_R^2}E_I.
\]

Hence

\[
\boxed{
P_\eta
\ge
\frac23\kappa_*e_*
-
\frac{C E_I}{L_R^2}.
}
\]

For all sufficiently large `R`,

\[
\boxed{
P_\eta\ge c_*>0.
}
\]

Thus mesoscopic transverse thickness restores a genuine palinstrophy lower bound without any local doubling assumption.

## 6. Ancestral consequence

Suppose this thick negative-kappa core persists for parent-time fraction `beta_R`, i.e. for order

\[
\beta_RR^2
\]

own-time units.

Then normalized palinstrophy spacetime cost is at least

\[
\gtrsim c_*\beta_RR^2.
\]

M17-307 applies ancestry weight `R^-1`, giving

\[
\boxed{
\mathcal P_{anc,R}
\gtrsim
c_*\beta_RR.
}
\]

Therefore finite ancestral palinstrophy requires

\[
\boxed{
\sum_m\beta_{R_m}R_m<\infty.
}
\]

A positive lower bound on `beta_R` is impossible.

## 7. Relation to M17-428

M17-428 remains correct for isolated own-scale cells: a unit-width cutoff has an order-one boundary error and cannot force coercivity.

M17-454 does not supersede that no-go.

It identifies a distinct regime:

\[
\boxed{
\text{negative-kappa region thickness }L_R\to\infty
}
\]

makes the cutoff error `O(L_R^-2)` and restores coercivity.

Thus mesoscopic broadening helps only when the negative-kappa sign region itself broadens with the flux carrier.

## 8. Updated diffuse branch split

A persistent diffuse positive-flux carrier cannot retain a mesoscopically thick negative-kappa region carrying fixed enstrophy mass.

Hence the negative-coefficient part must escape through at least one of

\[
\boxed{
\begin{aligned}
&G_{negative\text{-}kappa\ weighted\ enstrophy\ mass\ loss},\\
&G_{negative\text{-}kappa\ transverse\ thickness\ collapse},\\
&G_{rapid\ sign/zero\text{-}corridor\ fragmentation},\\
&G_{separator\ time\ thinning},\\
&G_{coefficient/high\text{-}jet\ decompactification},\\
&G_{chart/interface/genealogy\ loss}.
\end{aligned}
}
\]

The first branch is consistent with the M17-367 amplitude firewall: a substantial negative coefficient can live where vorticity amplitude is too small to pay palinstrophy.

## 9. Audit verdict

**PASS — mesoscopic sign thickness removes the local boundary firewall.**

If a negative-kappa sub-tube becomes wide in own-scale units and carries fixed enstrophy mass, wide-cutoff integration by parts forces order-one palinstrophy and the `R^-1` ancestral ledger closes persistent residence.

\[
\boxed{\text{GLOBAL 3D NAVIER--STOKES REGULARITY REMAINS UNPROVED.}}
\]
